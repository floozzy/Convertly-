from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from database.users import create_user


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    create_user(
        update.effective_user
    )

    keyboard = [

        [
            InlineKeyboardButton(
                "📂 Конвертировать",
                callback_data="convert"
            )
        ],

        [
            InlineKeyboardButton(
                "👤 Профиль",
                callback_data="profile"
            )
        ],

        [
            InlineKeyboardButton(
                "⭐ Premium",
                callback_data="premium"
            )
        ],

        [
            InlineKeyboardButton(
                "ℹ️ Помощь",
                callback_data="help"
            )
        ]

    ]

    await update.message.reply_text(

        "🚀 Добро пожаловать в Convertly!\n\n"
        "Самый удобный конвертер файлов.",

        reply_markup=InlineKeyboardMarkup(keyboard)

    )
