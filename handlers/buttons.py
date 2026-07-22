from telegram import Update
from telegram.ext import ContextTypes


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    if query.data == "convert":

        await query.edit_message_text(
            "📂 Отправьте мне файл.\n\n"
            "Я определю его формат и предложу варианты конвертации."
        )


    elif query.data == "profile":

        await query.edit_message_text(
            "👤 Ваш профиль:\n\n"
            "Файлов обработано: 0\n"
            "Статус: Бесплатный"
        )


    elif query.data == "help":

        await query.edit_message_text(
            "ℹ️ Convertly умеет работать с файлами.\n\n"
            "Скоро появятся:\n"
            "🖼 Изображения\n"
            "📄 PDF\n"
            "🎵 Аудио\n"
            "🎬 Видео"
        )
