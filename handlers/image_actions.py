import os

from telegram.ext import ContextTypes

from services.image.compress import compress_image
from services.image.convert import convert_image
from services.image.info import image_info

from database.history import add_history


UPLOAD_DIR = "files/uploads"



def get_last_image(
    user_id
):

    files = [

        f for f in os.listdir(UPLOAD_DIR)

        if f.startswith(
            str(user_id)
        )

    ]

    if not files:
        return None


    return os.path.join(
        UPLOAD_DIR,
        files[-1]
    )



async def image_compress_action(
    update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    user_id = query.from_user.id


    path = get_last_image(
        user_id
    )


    if not path:

        await query.message.reply_text(
            "❌ Фото не найдено."
        )

        return


    await query.message.reply_text(
        "📦 Сжимаю изображение..."
    )


    result = compress_image(
        path
    )


    add_history(
        user_id,
        path,
        "Сжатие изображения"
    )


    await query.message.reply_document(
        open(result, "rb"),
        caption="✅ Изображение сжато"
    )



async def image_info_action(
    update,
    context
):

    query = update.callback_query

    user_id = query.from_user.id


    path = get_last_image(
        user_id
    )


    if not path:

        await query.message.reply_text(
            "❌ Фото не найдено."
        )

        return


    data = image_info(
        path
    )


    await query.message.reply_text(

        "📊 Информация:\n\n"

        f"📄 {data['name']}\n"
        f"🖼 Формат: {data['format']}\n"
        f"📐 Размер: {data['width']}x{data['height']}\n"
        f"💾 Вес: {data['size']} MB"

    )



async def image_convert_action(
    update,
    context
):

    query = update.callback_query

    user_id = query.from_user.id


    path = get_last_image(
        user_id
    )


    if not path:

        await query.message.reply_text(
            "❌ Фото не найдено."
        )

        return


    result = convert_image(
        path,
        "png"
    )


    add_history(
        user_id,
        path,
        "JPG → PNG"
    )


    await query.message.reply_document(
        open(result,"rb"),
        caption="✅ Конвертация JPG → PNG готова"
    )
