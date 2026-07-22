from __future__ import annotations

import os


def get_bot_token() -> str:
    return os.getenv("BOT_TOKEN", "").strip()
