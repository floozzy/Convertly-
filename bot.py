import logging

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters
)

from config import TOKEN

from database.models import init_db

from handlers.start import start_command
from handlers.buttons import button_handler
from handlers.profile import profile_command
from handlers.files import file_handler


logging.basicConfig(
    level=logging.INFO
)


def main():

    init_db()


    app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )


    app.add_handler(
        CommandHandler(
            "start",
            start_command
        )
    )


    app.add_handler(
        CommandHandler(
            "profile",
            profile_command
        )
    )


    app.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )


    app.add_handler(
        MessageHandler(
            filters.Document.ALL,
            file_handler
        )
    )


    print(
        "🚀 Convertly запущен!"
    )


    app.run_polling()


if __name__ == "__main__":
    main()
