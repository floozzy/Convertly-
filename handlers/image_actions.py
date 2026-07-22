import os

from telegram import Update
from telegram.ext import ContextTypes

from services.image.compress import compress_image
from services.image.info import image_info

from database.history import add_history


UPLOAD_DIR = "files/uploads"


async def image_compress_action(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id


    files = [
        f for f in os.listdir(UPLOAD_DIR)
        if f.startswith(str(user_id))
    ]


    if not files:

        await query.message.reply_text(
            "❌ Не найдено изображение."
        )

        return


    filename = files[-1]


    path = os.path.join(
        UPLOAD_DIR,
        filename
    )


    await query.message.reply_text(
        "📦 Сжимаю изображение..."
    )


    result = compress_image(
        path
    )


    add_history(
        user_id,
        filename,
        "Сжатие изображения"
    )


    with open(
        result,
        "rb"
    ) as file:

        await query.message.reply_document(
            document=file,
            caption="✅ Готово! Изображение сжато."
        )
