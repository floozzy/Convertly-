import os

from config import settings


def test_load_env_file_reads_token(monkeypatch, tmp_path):
    env_path = tmp_path / ".env"
    env_path.write_text("BOT_TOKEN=from-test\n", encoding="utf-8")

    monkeypatch.delenv("BOT_TOKEN", raising=False)
    monkeypatch.setattr(settings, "BASE_DIR", tmp_path)

    settings.load_env_file()

    assert os.environ["BOT_TOKEN"] == "from-test"
