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

    if data == "convert":

        await query.message.reply_text(
            "📂 Отправьте мне файл для конвертации."
        )

    elif data == "profile":

        class FakeMessage:
            def __init__(self, message):
                self.reply_text = message.reply_text

        class FakeUpdate:
            def __init__(self, original):
                self.effective_user = original.effective_user
                self.message = FakeMessage(original.callback_query.message)

        await profile_command(
            FakeUpdate(update),
            context
        )

    elif data == "premium":

        await query.message.reply_text(
            "👑 Premium скоро появится.\n\n"
            "Покупка будет доступна за Telegram Stars ⭐"
        )

    elif data == "help":

        await query.message.reply_text(
            "📚 Convertly\n\n"
            "• Отправьте файл.\n"
            "• Выберите нужную конвертацию.\n"
            "• Получите готовый результат."
        )

    else:

        await query.message.reply_text(
            "⚠️ Неизвестная команда."
        )
