from telegram import Update
from telegram.ext import ContextTypes


from utils.state import (
    set_state,
    has_state
)



async def text_input_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):


    user_id = update.effective_user.id



    if has_state(
        user_id,
        "waiting_watermark_text"
    ):


        text = update.message.text



        set_state(

            user_id,

            "text",

            text

        )


        set_state(

            user_id,

            "waiting_watermark_text",

            False

        )


        await update.message.reply_text(

            "✅ Текст водяного знака изменён:\n\n"
            f"💧 {text}"

        )


        return
