from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class UserRecord:
    user_id: int
    username: str


@dataclass
class JobRecord:
    user_id: int
    operation: str
    status: str
    job_id: int | None = None


class SQLiteRepository:
    def __init__(self, db_path: str | Path):
        self.db_path = str(db_path)
        self._initialize()

    def _initialize(self) -> None:
        with sqlite3.connect(self.db_path) as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL
                )
                """
            )
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    operation TEXT NOT NULL,
                    status TEXT NOT NULL
                )
                """
            )
            connection.commit()

    def upsert_user(self, user_id: int, username: str) -> UserRecord:
        with sqlite3.connect(self.db_path) as connection:
            connection.execute(
                "INSERT INTO users(user_id, username) VALUES(?, ?) ON CONFLICT(user_id) DO UPDATE SET username=excluded.username",
                (user_id, username),
            )
            connection.commit()
            row = connection.execute(
                "SELECT user_id, username FROM users WHERE user_id = ?",
                (user_id,),
            ).fetchone()
        return UserRecord(user_id=row[0], username=row[1])

    def get_user(self, user_id: int) -> UserRecord | None:
        with sqlite3.connect(self.db_path) as connection:
            row = connection.execute(
                "SELECT user_id, username FROM users WHERE user_id = ?",
                (user_id,),
            ).fetchone()
        if row is None:
            return None
        return UserRecord(user_id=row[0], username=row[1])

    def create_job(self, user_id: int, operation: str) -> JobRecord:
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(
                "INSERT INTO jobs(user_id, operation, status) VALUES(?, ?, ?)",
                (user_id, operation, "queued"),
            )
            connection.commit()
            return JobRecord(user_id=user_id, operation=operation, status="queued", job_id=cursor.lastrowid)

    def list_jobs(self, user_id: int) -> list[JobRecord]:
        with sqlite3.connect(self.db_path) as connection:
            rows = connection.execute(
                "SELECT id, user_id, operation, status FROM jobs WHERE user_id = ?",
                (user_id,),
            ).fetchall()
        return [JobRecord(user_id=row[1], operation=row[2], status=row[3], job_id=row[0]) for row in rows]
