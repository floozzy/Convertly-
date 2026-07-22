from telegram import Update
from telegram.ext import ContextTypes


async def file_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.document:

        filename = update.message.document.file_name

        await update.message.reply_text(
            "📥 Файл получен!\n\n"
            f"📄 {filename}\n\n"
            "⚙️ Скоро начну обработку."
        )
