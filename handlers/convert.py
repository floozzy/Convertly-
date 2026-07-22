from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from services.image_tools import (
    convert_image,
    compress_image,
    resize_image
)


async def convert_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


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
                "📦 Сжать изображение",
                callback_data="compress"
            )
        ]
    ]


    await query.edit_message_text(
        "⚙️ Выберите действие:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
