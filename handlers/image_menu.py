from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def image_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    keyboard = [

        [
            InlineKeyboardButton(
                "🔄 Конвертация",
                callback_data="img_convert"
            )
        ],

        [
            InlineKeyboardButton(
                "📦 Сжать",
                callback_data="img_compress"
            )
        ],

        [
            InlineKeyboardButton(
                "📐 Размер",
                callback_data="img_resize"
            )
        ],

        [
            InlineKeyboardButton(
                "✨ Эффекты",
                callback_data="img_effects"
            )
        ],

        [
            InlineKeyboardButton(
                "💧 Водяной знак",
                callback_data="img_watermark"
            )
        ],

        [
            InlineKeyboardButton(
                "📊 Информация",
                callback_data="img_info"
            )
        ]

    ]


    await update.message.reply_text(

        "🖼 <b>Image Engine</b>\n\n"
        "Выберите действие:",

        reply_markup=InlineKeyboardMarkup(keyboard),

        parse_mode="HTML"
    )
