import os

import app.services.telegram_runtime as telegram_runtime


def test_configure_runtime_loads_env_from_repo_root(monkeypatch, tmp_path) -> None:
    project_root = tmp_path / "repo"
    services_dir = project_root / "app" / "services"
    services_dir.mkdir(parents=True)
    (project_root / ".env").write_text("BOT_TOKEN=demo-token\n", encoding="utf-8")
    monkeypatch.setattr(telegram_runtime, "__file__", str(services_dir / "telegram_runtime.py"))
    monkeypatch.delenv("BOT_TOKEN", raising=False)

    telegram_runtime.configure_runtime()

    assert os.getenv("BOT_TOKEN") == "demo-token"
