from telegram.ext import ContextTypes

from handlers.image_actions import (
    image_compress_action,
    image_info_action,
    image_convert_action
)


async def button_handler(
    update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    data = query.data


    # =====================
    # MAIN MENU
    # =====================


    if data == "convert":

        await query.message.reply_text(
            "📂 Отправьте файл для обработки."
        )


    elif data == "profile":

        await query.message.reply_text(
            "👤 Профиль\n\n"
            "Используйте команду:\n"
            "/profile"
        )


    elif data == "premium":

        await query.message.reply_text(
            "⭐ Convertly Premium\n\n"
            "Скоро будет доступно:\n\n"
            "🚀 Больше лимитов\n"
            "⚡ Быстрее обработка\n"
            "🤖 AI-функции\n"
            "📦 Большие файлы"
        )


    elif data == "help":

        await query.message.reply_text(
            "ℹ️ Помощь Convertly\n\n"
            "1. Отправьте файл\n"
            "2. Выберите действие\n"
            "3. Получите результат"
        )


    # =====================
    # IMAGE ENGINE
    # =====================


    elif data == "img_convert":

        await image_convert_action(
            update,
            context
        )


    elif data == "img_compress":

        await image_compress_action(
            update,
            context
        )


    elif data == "img_info":

        await image_info_action(
            update,
            context
        )


    elif data == "img_resize":

        await query.message.reply_text(
            "📐 Resize Engine\n\n"
            "В разработке."
        )


    elif data == "img_effects":

        await query.message.reply_text(
            "✨ Effects Engine\n\n"
            "В разработке."
        )


    elif data == "img_watermark":

        await query.message.reply_text(
            "💧 Watermark Engine\n\n"
            "В разработке."
        )


    else:

        await query.message.reply_text(
            "⚠️ Неизвестная команда:\n"
            f"{data}"
        )
