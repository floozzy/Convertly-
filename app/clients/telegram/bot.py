from __future__ import annotations

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from app.services.bot_service import build_help_message, build_start_message
from app.services.token_service import get_bot_token
from config.settings import BOT_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(build_start_message())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(build_help_message())


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Image received. Processing will be added soon.")


def build_app() -> Application:
    token = BOT_TOKEN or get_bot_token()
    if not token:
        raise RuntimeError("BOT_TOKEN is not set")

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    return application


def main() -> None:
    app = build_app()
    app.run_polling()
