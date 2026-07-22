import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def file_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    document = update.message.document

    if not document:
        return


    filename = document.file_name

    file = await document.get_file()


    path = f"files/{filename}"


    await file.download_to_drive(
        path
    )


    context.user_data["file"] = path


    keyboard = [
        [
            InlineKeyboardButton(
                "🖼 JPG → PNG",
                callback_data="jpg_png"
            )
        ],
        [
            InlineKeyboardButton(
                "🖼 PNG → JPG",
                callback_data="png_jpg"
            )
        ],
        [
            InlineKeyboardButton(
                "📦 Сжать",
                callback_data="compress"
            )
        ]
    ]


    await update.message.reply_text(
        "📥 Файл получен!\n\n"
        f"📄 {filename}\n\n"
        "Выберите действие:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
