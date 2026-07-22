import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def load_env_file() -> None:
    env_path = BASE_DIR / ".env"
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


load_env_file()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
APP_NAME = os.getenv("APP_NAME", "Convertly")
STORAGE_DIR = BASE_DIR / "storage"
STORAGE_DIR.mkdir(exist_ok=True)
