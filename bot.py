from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters
)


from handlers.start import start_command
from handlers.profile import profile_command
from handlers.buttons import button_handler
from handlers.image_actions import photo_handler
from handlers.text_input import text_input_handler



# ==========================
# BOT TOKEN
# ==========================

TOKEN = "8831427693:AAED6ZtuPdcZnvsAvku-DPNSZ_QsBNzrc0I"





# ==========================
# START
# ==========================

def main():

    app = Application.builder().token(
        TOKEN
    ).build()



    # ==========================
    # COMMANDS
    # ==========================


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



    # ==========================
    # PHOTOS
    # ==========================


    app.add_handler(
        MessageHandler(
            filters.PHOTO | filters.Document.IMAGE,
            photo_handler
        )
    )


    print(
        "✅ PHOTO HANDLER ADDED"
    )



    # ==========================
    # BUTTONS
    # ==========================


    app.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )



    # ==========================
    # TEXT INPUT
    # ==========================


    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            text_input_handler
        )
    )



    print(
        "🚀 Convertly запущен успешно!"
    )



    app.run_polling()





if __name__ == "__main__":
    main()
