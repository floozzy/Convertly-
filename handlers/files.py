import os

from telegram import Update
from telegram.ext import ContextTypes

from database.history import add_history
from database.users import add_file

from handlers.image_menu import image_menu


UPLOAD_DIR = "files/uploads"


os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)



async def file_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    document = update.message.document

    if not document:
        return


    user_id = update.effective_user.id

    filename = document.file_name


    path = os.path.join(
        UPLOAD_DIR,
        f"{user_id}_{filename}"
    )


    telegram_file = await document.get_file()


    await telegram_file.download_to_drive(
        path
    )


    add_file(
        user_id
    )


    add_history(
        user_id,
        filename,
        "Загрузка файла"
    )


    extension = filename.lower().split(".")[-1]


    if extension in [
        "jpg",
        "jpeg",
        "png",
        "webp",
        "bmp"
    ]:

        await image_menu(
            update,
            context
        )

    else:

        await update.message.reply_text(

            "✅ Файл получен!\n\n"
            f"📄 {filename}\n\n"
            "⚙️ Поддержка этого формата скоро появится."

        )
