import os


from telegram import Update
from telegram.ext import ContextTypes


from services.image.info import image_info


from utils.images import (
    save_image,
    get_image
)


from utils.state import (
    set_state,
    get_state,
    clear_state
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

    print(
        "🔥 PHOTO HANDLER WORKS"
    )


    try:

        user_id = update.effective_user.id



        # ==============================
        # CONVERT MODE
        # ==============================


        if get_state(

            user_id,

            "waiting_convert_photo"

        ):


            clear_state(

                user_id,

                "waiting_convert_photo"

            )


            await update.message.reply_text(

                "🔄 Фото получено!\n"
                "Запускаю конвертацию..."

            )


            print(

                "CONVERT PHOTO RECEIVED"

            )


            return





        # ==============================
        # WATERMARK MODE
        # ==============================


        if get_state(

            user_id,

            "waiting_watermark_photo"

        ):


            clear_state(

                user_id,

                "waiting_watermark_photo"

            )


            await update.message.reply_text(

                "💧 Фото получено!\n"
                "Добавляю водяной знак..."

            )


            print(

                "WATERMARK PHOTO RECEIVED"

            )


            return






        # ==============================
        # NORMAL SAVE
        # ==============================


        photo = update.message.photo[-1]



        telegram_file = await context.bot.get_file(

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



        await telegram_file.download_to_drive(

            path

        )



        save_image(

            user_id,

            path

        )



        print(

            "IMAGE SAVED:",

            path

        )



        await update.message.reply_text(

            "✅ Фото получено!\n"
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
# INFO
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

            "❌ Сначала отправьте фотографию."

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



    set_state(

        user_id,

        "waiting_convert_photo",

        True

    )



    await query.message.reply_text(

        "🔄 <b>Конвертация</b>\n\n"
        "📷 Отправьте фотографию.",

        parse_mode="HTML"

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



    set_state(

        user_id,

        "waiting_compress_photo",

        True

    )



    await query.message.reply_text(

        "🗜 <b>Сжатие</b>\n\n"
        "📷 Отправьте фотографию.",

        parse_mode="HTML"

    )
