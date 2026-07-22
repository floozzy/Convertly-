from telegram.ext import ContextTypes

from handlers.image_actions import (
    image_compress_action,
    image_info_action,
    image_convert_action
)


async def button_handler(
    update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    data = query.data



    if data == "img_compress":

        await image_compress_action(
            update,
            context
        )


    elif data == "img_info":

        await image_info_action(
            update,
            context
        )


    elif data == "img_convert":

        await image_convert_action(
            update,
            context
        )


    elif data == "img_resize":

        await query.message.reply_text(
            "📐 Resize Engine скоро."
        )


    elif data == "img_effects":

        await query.message.reply_text(
            "✨ Effects Engine скоро."
        )


    elif data == "img_watermark":

        await query.message.reply_text(
            "💧 Watermark Engine скоро."
        )


    else:

        await query.message.reply_text(
            "⚠️ Команда не найдена."
        )
