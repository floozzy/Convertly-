from __future__ import annotations

import os

from telegram import Bot


def get_bot_username() -> str:
    token = os.getenv("BOT_TOKEN", "")
    return f"bot:{token[:10]}..." if token else "bot:unset"


def check_bot_connection() -> bool:
    token = os.getenv("BOT_TOKEN", "")
    if not token:
        return False
    bot = Bot(token=token)
    try:
        bot.get_me()
        return True
    except Exception:
        return False
