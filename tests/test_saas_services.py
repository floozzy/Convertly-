import sqlite3

from app.repositories.sqlite_repository import SQLiteRepository
from app.services.job_service import JobService
from app.services.user_service import UserService


def test_user_service_creates_and_reads_user(tmp_path):
    db_path = tmp_path / "users.sqlite3"
    repository = SQLiteRepository(str(db_path))
    service = UserService(repository)

    user = service.get_or_create_user(42, "alice")

    assert user.user_id == 42
    assert user.username == "alice"
    assert service.get_user(42).username == "alice"


def test_job_service_persists_jobs(tmp_path):
    db_path = tmp_path / "jobs.sqlite3"
    repository = SQLiteRepository(str(db_path))
    service = JobService(repository)

    job = service.create_job(42, "grayscale")

    assert job.user_id == 42
    assert job.operation == "grayscale"
    assert job.status == "queued"
    assert len(service.list_jobs(42)) == 1
