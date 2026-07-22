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



    # =========================
    # IMAGE INFORMATION
    # =========================

    if data == "info":

        await image_info_action(
            update,
            context
        )

        return



    # =========================
    # CONVERT IMAGE
    # =========================

    if data == "convert":

        await image_convert_action(
            update,
            context
        )

        return



    # =========================
    # COMPRESS IMAGE
    # =========================

    if data == "compress":

        await image_compress_action(
            update,
            context
        )

        return



    # =========================
    # WATERMARK
    # =========================

    if data == "watermark":

        await watermark_action(
            update,
            context
        )

        return



    # =========================
    # UNKNOWN BUTTON
    # =========================

    await query.message.reply_text(

        "❌ Неизвестная команда.\n"
        "Эта функция ещё не подключена."

    )
