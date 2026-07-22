from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)

from config import TOKEN

from handlers.start import start_command
from handlers.files import file_handler
from handlers.buttons import button_handler


def main():

    app = Application.builder().token(TOKEN).build()


    # Команда /start
    app.add_handler(
        CommandHandler(
            "start",
            start_command
        )
    )


    # Получение файлов
    app.add_handler(
        MessageHandler(
            filters.Document.ALL,
            file_handler
        )
    )


    # Обработка кнопок
    app.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )


    print("🚀 Convertly запущен успешно!")


    app.run_polling()


if __name__ == "__main__":
    main()
