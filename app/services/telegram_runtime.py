from __future__ import annotations

import logging
import os
from pathlib import Path

from app.services.token_service import get_bot_token


def configure_runtime() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    base_dir = Path(__file__).resolve().parent.parent
    env_path = base_dir / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())

    token = get_bot_token()
    if not token:
        raise RuntimeError("BOT_TOKEN is missing. Add it to .env")
