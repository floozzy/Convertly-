from __future__ import annotations

from app.repositories.sqlite_repository import SQLiteRepository, UserRecord


class UserService:
    def __init__(self, repository: SQLiteRepository):
        self.repository = repository

    def get_or_create_user(self, user_id: int, username: str) -> UserRecord:
        existing = self.repository.get_user(user_id)
        if existing is not None:
            return existing
        return self.repository.upsert_user(user_id, username)

    def get_user(self, user_id: int) -> UserRecord | None:
        return self.repository.get_user(user_id)
