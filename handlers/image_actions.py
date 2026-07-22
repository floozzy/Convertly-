import os


from telegram import Update
from telegram.ext import ContextTypes


from services.image.info import image_info


from utils.images import (
    save_image,
    get_image
)



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





# =====================================
# PHOTO HANDLER
# =====================================


async def photo_handler(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):

    try:


        user_id = update.effective_user.id


        print(
            "PHOTO RECEIVED:",
            user_id
        )



        photo = update.message.photo[-1]



        telegram_file = await context.bot.get_file(

            photo.file_id

        )



        filename = (

            str(user_id)

            +

            "_"

            +

            str(photo.file_id)

            +

            ".jpg"

        )



        path = os.path.join(

            UPLOAD_DIR,

            filename

        )



        await telegram_file.download_to_drive(

            path

        )



        save_image(

            user_id,

            path

        )



        await update.message.reply_text(

            "✅ Фото получено!\n\n"
            "Теперь выберите действие."

        )


        print(

            "IMAGE SAVED:",

            path

        )



    except Exception as e:


        print(

            "PHOTO ERROR:",

            e

        )


        await update.message.reply_text(

            "❌ Ошибка загрузки фото:\n"

            +

            str(e)

        )







# =====================================
# IMAGE INFO
# =====================================


async def image_info_action(

    update,

    context

):


    query = update.callback_query


    user_id = query.from_user.id



    path = get_image(

        user_id

    )



    if not path:


        await query.message.reply_text(

            "❌ Фото не найдено.\n"
            "Сначала отправьте фотографию."

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


        print(

            "INFO ERROR:",

            e

        )


        await query.message.reply_text(

            "❌ Ошибка анализа фото:\n"

            +

            str(e)

        )







# =====================================
# CONVERT
# =====================================


async def image_convert_action(

    update,

    context

):


    query = update.callback_query


    user_id = query.from_user.id



    path = get_image(

        user_id

    )



    if not path:


        await query.message.reply_text(

            "❌ Фото не найдено."

        )


        return



    await query.message.reply_text(

        "🔄 Конвертация пока подключается."

    )








# =====================================
# COMPRESS
# =====================================


async def image_compress_action(

    update,

    context

):


    query = update.callback_query


    user_id = query.from_user.id



    path = get_image(

        user_id

    )



    if not path:


        await query.message.reply_text(

            "❌ Фото не найдено."

        )


        return



    await query.message.reply_text(

        "🗜 Сжатие пока подключается."

    )
