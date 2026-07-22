from __future__ import annotations

import logging

from telegram import Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from app.services.bot_service import build_help_message, build_start_message
from app.services.menu_service import build_main_menu, build_photo_menu
from app.services.telegram_runtime import configure_runtime
from app.services.token_service import get_bot_token
from config.settings import BOT_TOKEN

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(build_start_message(), reply_markup=build_main_menu())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(build_help_message(), reply_markup=build_main_menu())


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("📸 Фото получено. Выберите действие:", reply_markup=build_photo_menu())


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query is None:
        return

    await query.answer()
    data = query.data or ""

    if data == "action:photo":
        await query.edit_message_text("🖼 Выберите операцию для фото", reply_markup=build_photo_menu())
    elif data == "action:pdf":
        await query.edit_message_text("📄 PDF tools coming soon", reply_markup=build_main_menu())
    elif data == "action:ai":
        await query.edit_message_text("🤖 AI tools coming soon", reply_markup=build_main_menu())
    elif data == "action:help":
        await query.edit_message_text(build_help_message(), reply_markup=build_main_menu())
    elif data == "action:main":
        await query.edit_message_text(build_start_message(), reply_markup=build_main_menu())
    elif data.startswith("op:"):
        operation = data.split(":", 1)[1]
        await query.edit_message_text(f"⚙️ Выбрана операция: {operation}", reply_markup=build_main_menu())


def build_app() -> Application:
    configure_runtime()
    token = BOT_TOKEN or get_bot_token()
    if not token:
        raise RuntimeError("BOT_TOKEN is not set")

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(CallbackQueryHandler(handle_callback))
    return application


def main() -> None:
    logger.info("Starting Convertly Telegram bot...")
    app = build_app()
    logger.info("Telegram bot connected and polling for updates")
    app.run_polling()
