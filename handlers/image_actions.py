import os


from telegram import Update
from telegram.ext import ContextTypes


from utils.images import (
    save_image,
    get_image
)

from utils.state import (
    set_state,
    get_state,
    clear_state
)


from services.image.info import image_info



UPLOAD_DIR = "files/uploads"


os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)





# ==================================================
# RECEIVE PHOTO
# ==================================================


async def photo_handler(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):

    print(
        "🔥 PHOTO HANDLER WORKS"
    )


    user_id = update.effective_user.id



    try:


        # ==========================
        # CONVERT MODE
        # ==========================


        if get_state(

            user_id,

            "waiting_convert_photo"

        ):


            clear_state(

                user_id,

                "waiting_convert_photo"

            )



            photo = update.message.photo[-1]



            tg_file = await context.bot.get_file(

                photo.file_id

            )



            path = os.path.join(

                UPLOAD_DIR,

                f"{user_id}_convert.jpg"

            )



            await tg_file.download_to_drive(

                path

            )



            save_image(

                user_id,

                path

            )



            print(

                "CONVERT IMAGE:",

                path

            )



            await update.message.reply_text(

                "🔄 Фото получено!\n"
                "Конвертация запущена..."

            )



            # ВРЕМЕННО ТЕСТ
            # потом заменим настоящим конвертером


            with open(

                path,

                "rb"

            ) as img:


                await update.message.reply_photo(

                    img,

                    caption="✅ Конвертация завершена (тест)"

                )



            return







        # ==========================
        # WATERMARK MODE
        # ==========================


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
                "Watermark запускается..."

            )


            return








        # ==========================
        # NORMAL PHOTO
        # ==========================



        photo = update.message.photo[-1]



        tg_file = await context.bot.get_file(

            photo.file_id

        )



        path = os.path.join(

            UPLOAD_DIR,

            f"{user_id}_{photo.file_id}.jpg"

        )



        await tg_file.download_to_drive(

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

            "✅ Фото сохранено!\n"
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








# ==================================================
# IMAGE INFO
# ==================================================


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








# ==================================================
# CONVERT BUTTON
# ==================================================


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








# ==================================================
# COMPRESS BUTTON
# ==================================================


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
