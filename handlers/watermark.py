from telegram.ext import ContextTypes

from services.image.watermark import add_watermark

from handlers.image_actions import get_last_image



async def watermark_action(
    update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query


    await query.answer()



    path = get_last_image(

        query.from_user.id

    )



    if not path:


        await query.message.reply_text(

            "❌ Сначала отправьте изображение."

        )

        return




    await query.message.reply_text(

        "💧 Добавляю водяной знак..."

    )



    result = add_watermark(

        path,

        text="© Convertly",

        position="bottom_right",

        color=(255,255,255),

        opacity=120,

        font_size=50

    )



    if not result:


        await query.message.reply_text(

            "❌ Не удалось создать watermark."

        )

        return




    with open(

        result,

        "rb"

    ) as file:


        await query.message.reply_document(

            document=file,

            caption="✅ Водяной знак добавлен"

        )
