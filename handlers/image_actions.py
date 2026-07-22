import os


from telegram import Update
from telegram.ext import ContextTypes


from services.image.info import image_info


from utils.images import (
    save_image,
    get_image
)



UPLOAD_DIR = "files/uploads"


os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)





# =====================================
# PHOTO HANDLER
# =====================================


async def photo_handler(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):

    print("🔥 PHOTO HANDLER WORKS")


    try:

        user_id = update.effective_user.id


        print(
            "USER:",
            user_id
        )



        photo = update.message.photo[-1]



        file = await context.bot.get_file(

            photo.file_id

        )



        filename = (

            f"{user_id}_"

            f"{photo.file_id}.jpg"

        )



        path = os.path.join(

            UPLOAD_DIR,

            filename

        )



        await file.download_to_drive(

            path

        )



        save_image(

            user_id,

            path

        )



        print(

            "PHOTO SAVED:",

            path

        )



        await update.message.reply_text(

            "✅ Фото получено!\n\n"
            "Выберите действие 👇"

        )



    except Exception as e:


        print(

            "PHOTO ERROR:",

            e

        )


        await update.message.reply_text(

            "❌ Ошибка обработки фото:\n"

            + str(e)

        )







# =====================================
# IMAGE INFO
# =====================================


async def image_info_action(

    update,

    context

):

    query = update.callback_query


    await query.answer()



    user_id = query.from_user.id



    path = get_image(

        user_id

    )



    if not path:


        await query.message.reply_text(

            "❌ Фото не найдено.\n"
            "Сначала отправьте изображение."

        )


        return



    try:


        result = image_info(

            path

        )



        await query.message.reply_text(

            result

        )



    except Exception as e:


        print(

            "INFO ERROR:",

            e

        )


        await query.message.reply_text(

            "❌ Ошибка анализа:\n"

            + str(e)

        )






# =====================================
# CONVERT
# =====================================


async def image_convert_action(

    update,

    context

):

    query = update.callback_query


    await query.answer()



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

        "🔄 Конвертация подключается."

    )







# =====================================
# COMPRESS
# =====================================


async def image_compress_action(

    update,

    context

):

    query = update.callback_query


    await query.answer()



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

        "🗜 Сжатие подключается."

    )
