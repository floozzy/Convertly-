from telegram import Update
from telegram.ext import ContextTypes

from handlers.convert import convert_menu


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    if query.data == "convert":

        await convert_menu(
            update,
            context
        )


    elif query.data == "profile":

        await query.edit_message_text(
            "👤 Профиль\n\n"
            "Файлов обработано: 0\n"
            "Статус: Free"
        )


    elif query.data == "help":

        await query.edit_message_text(
            "ℹ️ Convertly 3.1\n\n"
            "Поддерживаемые функции:\n"
            "🖼 Изображения\n"
            "📄 PDF (скоро)\n"
            "🎵 Аудио (скоро)"
        )
