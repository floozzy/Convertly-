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
from handlers.convert import convert_menu


def main():

    app = Application.builder().token(TOKEN).build()


    app.add_handler(
        CommandHandler(
            "start",
            start_command
        )
    )


    app.add_handler(
        MessageHandler(
            filters.Document.ALL,
            file_handler
        )
    )


    app.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )


    print("🚀 Convertly 3.0 запущен!")


    app.run_polling()


if __name__ == "__main__":
    main()
