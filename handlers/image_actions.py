import os
from pathlib import Path


from telegram import Update
from telegram.ext import ContextTypes



from services.image.info import image_info


# ==========================
# STORAGE
# ==========================


LAST_IMAGES = {}



UPLOAD_DIR = "files/uploads"

PROCESSED_DIR = "files/processed"



os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


os.makedirs(
    PROCESSED_DIR,
    exist_ok=True
)




def save_last_image(

    user_id,

    path

):

    LAST_IMAGES[user_id] = path




def get_last_image(

    user_id

):

    return LAST_IMAGES.get(
        user_id
    )





# ==========================
# PHOTO HANDLER
# ==========================


async def photo_handler(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):


    user_id = update.effective_user.id



    photo = update.message.photo[-1]



    file = await context.bot.get_file(

        photo.id

    )



    filename = (

        f"{user_id}_"

        f"{photo.id}.jpg"

    )



    path = os.path.join(

        UPLOAD_DIR,

        filename

    )



    await file.download_to_drive(

        path

    )



    save_last_image(

        user_id,

        path

    )



    await update.message.reply_text(

        "✅ Фото сохранено.\n\n"
        "Выберите действие:",

    )



    print(

        "IMAGE SAVED:",

        path

    )





# ==========================
# IMAGE INFO
# ==========================


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

            "❌ Сначала отправьте фото."

        )

        return



    try:


        data = image_info(

            path

        )



        await query.message.reply_text(

            data

        )



    except Exception as e:


        await query.message.reply_text(

            "❌ Ошибка анализа фото:\n"

            f"{e}"

        )





# ==========================
# CONVERT
# ==========================


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

            "❌ Сначала отправьте фото."

        )

        return




    await query.message.reply_text(

        "🔄 Конвертация пока подключается."

    )





# ==========================
# COMPRESS
# ==========================


async def image_compress_action(

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

            "❌ Сначала отправьте фото."

        )

        return




    await query.message.reply_text(

        "🗜 Сжатие пока подключается."

        )
