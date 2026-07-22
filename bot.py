import logging

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler
)

from config import TOKEN

from database.models import init_db

from handlers.start import start_command
from handlers.buttons import button_handler
from handlers.profile import profile_command


logging.basicConfig(
    level=logging.INFO
)


def main():

    print("🔄 Запуск базы данных...")

    init_db()

    print("✅ База данных готова")


    app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )


    # Команда /start
    app.add_handler(
        CommandHandler(
            "start",
            start_command
        )
    )


    # Команда /profile
    app.add_handler(
        CommandHandler(
            "profile",
            profile_command
        )
    )


    # Кнопки меню
    app.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )


    print(
        "🚀 Convertly запущен!"
    )


    app.run_polling()


if __name__ == "__main__":
    main()
