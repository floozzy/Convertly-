import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
APP_NAME = os.getenv("APP_NAME", "Convertly")
STORAGE_DIR = BASE_DIR / "storage"
STORAGE_DIR.mkdir(exist_ok=True)
