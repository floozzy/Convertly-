from telegram import Update
from telegram.ext import ContextTypes


from handlers.image_actions import (
    image_info_action,
    image_convert_action,
    image_compress_action
)


from handlers.watermark import (
    watermark_action
)



async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query


    await query.answer()



    data = query.data


    print(
        "BUTTON PRESSED:",
        data
    )



    # =========================
    # IMAGE INFO
    # =========================

    if data in [
        "img_info",
        "info"
    ]:

        await image_info_action(
            update,
            context
        )

        return



    # =========================
    # IMAGE CONVERT
    # =========================

    if data in [
        "img_convert",
        "convert"
    ]:

        await image_convert_action(
            update,
            context
        )

        return



    # =========================
    # IMAGE COMPRESS
    # =========================

    if data in [
        "img_compress",
        "compress"
    ]:

        await image_compress_action(
            update,
            context
        )

        return



    # =========================
    # WATERMARK
    # =========================

    if data in [
        "img_watermark",
        "watermark"
    ]:

        await watermark_action(
            update,
            context
        )

        return



    # =========================
    # UNKNOWN
    # =========================

    await query.message.reply_text(

        "❌ Функция пока не подключена.\n\n"
        f"Код кнопки: {data}"

    )
