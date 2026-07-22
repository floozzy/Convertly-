from telegram import Update
from telegram.ext import ContextTypes

from handlers.profile import profile_command


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    data = query.data


    if data == "profile":

        await query.message.reply_text(
            "Используйте команду:\n/profile"
        )


    elif data == "help":

        await query.message.reply_text(
            "📚 Convertly\n\n"
            "Отправьте файл, и я помогу его обработать."
        )


    elif data == "premium":

        await query.message.reply_text(
            "⭐ Premium скоро будет доступен."
        )


    elif data == "convert":

        await query.message.reply_text(
            "📂 Отправьте файл для обработки."
        )


    # IMAGE ENGINE

    elif data == "img_convert":

        await query.message.reply_text(
            "🔄 Конвертация изображений\n\n"
            "Скоро здесь будет выбор формата:\n"
            "JPG → PNG\n"
            "PNG → JPG\n"
            "WEBP → JPG"
        )


    elif data == "img_compress":

        await query.message.reply_text(
            "📦 Сжатие изображения\n\n"
            "Функция подключается."
        )


    elif data == "img_resize":

        await query.message.reply_text(
            "📐 Изменение размера\n\n"
            "Выберите размер в следующем обновлении."
        )


    elif data == "img_effects":

        await query.message.reply_text(
            "✨ Эффекты:\n\n"
            "• Ч/Б\n"
            "• Размытие\n"
            "• Отражение"
        )


    elif data == "img_watermark":

        await query.message.reply_text(
            "💧 Водяной знак\n\n"
            "Готовлю обработку."
        )


    elif data == "img_info":

        await query.message.reply_text(
            "📊 Информация об изображении\n\n"
            "Размеры и формат будут показаны здесь."
        )


    else:

        await query.message.reply_text(
            "⚠️ Неизвестная команда."
        )
