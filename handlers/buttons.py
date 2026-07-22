from telegram import Update
from telegram.ext import ContextTypes

from handlers.image_actions import image_compress_action


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    data = query.data


    # Главное меню

    if data == "convert":

        await query.message.reply_text(
            "📂 Отправьте файл для обработки."
        )


    elif data == "profile":

        await query.message.reply_text(
            "👤 Ваш профиль:\n\n"
            "Используйте команду:\n"
            "/profile"
        )


    elif data == "premium":

        await query.message.reply_text(
            "⭐ Premium Convertly\n\n"
            "Скоро появятся:\n"
            "• больше лимитов\n"
            "• быстрые серверы\n"
            "• AI-функции\n"
            "• обработка больших файлов"
        )


    elif data == "help":

        await query.message.reply_text(
            "ℹ️ Помощь Convertly\n\n"
            "Отправьте файл и выберите действие."
        )


    # IMAGE ENGINE


    elif data == "img_convert":

        await query.message.reply_text(
            "🔄 Конвертация изображений\n\n"
            "Доступно скоро:\n"
            "JPG → PNG\n"
            "PNG → JPG\n"
            "WEBP → JPG"
        )


    elif data == "img_compress":

        await image_compress_action(
            update,
            context
        )


    elif data == "img_resize":

        await query.message.reply_text(
            "📐 Изменение размера\n\n"
            "Модуль Resize Engine подключается."
        )


    elif data == "img_effects":

        await query.message.reply_text(
            "✨ Image Effects\n\n"
            "Будут доступны:\n"
            "• Ч/Б\n"
            "• Размытие\n"
            "• Отражение\n"
            "• Улучшение качества"
        )


    elif data == "img_watermark":

        await query.message.reply_text(
            "💧 Watermark Engine\n\n"
            "Добавление водяных знаков скоро."
        )


    elif data == "img_info":

        await query.message.reply_text(
            "📊 Image Info\n\n"
            "Покажу:\n"
            "• размер\n"
            "• формат\n"
            "• вес\n"
            "• разрешение"
        )


    else:

        await query.message.reply_text(
            "⚠️ Неизвестная команда."
        )
