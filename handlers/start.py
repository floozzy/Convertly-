from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "📂 Конвертировать файл",
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
                "ℹ️ Помощь",
                callback_data="help"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🚀 Добро пожаловать в Convertly 3.0!\n\n"
        "Я универсальный бот-конвертер файлов.\n\n"
        "Выберите действие:",
        reply_markup=reply_markup
    )
