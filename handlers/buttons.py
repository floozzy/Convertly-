from telegram import Update
from telegram.ext import ContextTypes

from utils.state import get_file
from services.image_tools import (
    convert_image,
    compress_image
)


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id


    path = get_file(user_id)


    if query.data in [
        "jpg_png",
        "png_jpg",
        "compress"
    ]:


        if not path:

            await query.edit_message_text(
                "❌ Сначала отправьте файл."
            )

            return


    if query.data == "jpg_png":

        result = convert_image(
            path,
            "png"
        )

        await query.message.reply_document(
            document=open(result, "rb"),
            caption="✅ JPG → PNG готово!"
        )


    elif query.data == "png_jpg":

        result = convert_image(
            path,
            "jpg"
        )

        await query.message.reply_document(
            document=open(result, "rb"),
            caption="✅ PNG → JPG готово!"
        )


    elif query.data == "compress":

        result = compress_image(
            path
        )

        await query.message.reply_document(
            document=open(result, "rb"),
            caption="✅ Изображение сжато!"
        )
