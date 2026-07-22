from __future__ import annotations

from app.repositories.sqlite_repository import JobRecord, SQLiteRepository


class JobService:
    def __init__(self, repository: SQLiteRepository):
        self.repository = repository

    def create_job(self, user_id: int, operation: str) -> JobRecord:
        return self.repository.create_job(user_id, operation)

    def list_jobs(self, user_id: int) -> list[JobRecord]:
        return self.repository.list_jobs(user_id)
