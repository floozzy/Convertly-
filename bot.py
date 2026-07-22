import logging

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)

from config import TOKEN

from database.models import init_db

from handlers.start import start_command
from handlers.buttons import button_handler


logging.basicConfig(
    level=logging.INFO
)


def main():

    print("🔄 Инициализация базы...")

    init_db()

    print("✅ База готова")


    app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )


    # /start
    app.add_handler(
        CommandHandler(
            "start",
            start_command
        )
    )


    # кнопки
    app.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )


    print(
        "🚀 Convertly запущен успешно!"
    )


    app.run_polling()


if __name__ == "__main__":
    main()
