from telegram import Update
from telegram.ext import ContextTypes


from handlers.image_actions import (
    image_info_action,
    image_convert_action,
    image_compress_action
)


from handlers.watermark import (
    watermark_action,
    watermark_apply
)


from utils.state import (
    set_state
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


    user_id = query.from_user.id



    # ==========================
    # IMAGE INFO
    # ==========================

    if data in [
        "img_info",
        "info"
    ]:


        await image_info_action(
            update,
            context
        )

        return




    # ==========================
    # CONVERT
    # ==========================

    if data in [
        "img_convert",
        "convert"
    ]:


        await image_convert_action(
            update,
            context
        )

        return




    # ==========================
    # COMPRESS
    # ==========================

    if data in [
        "img_compress",
        "compress"
    ]:


        await image_compress_action(
            update,
            context
        )

        return




    # ==========================
    # WATERMARK OPEN
    # ==========================

    if data in [
        "img_watermark",
        "watermark"
    ]:


        await watermark_action(
            update,
            context
        )

        return




    # ==========================
    # WATERMARK CREATE
    # ==========================

    if data == "wm_apply":


        await watermark_apply(
            update,
            context
        )

        return




    # ==========================
    # WATERMARK POSITION
    # ==========================

    if data == "wm_position":


        keyboard = [

            [

                ("↖️ Верх слева","tl"),

                ("⬆️ Верх центр","tc"),

                ("↗️ Верх справа","tr")

            ],

            [

                ("🎯 Центр","c")

            ],

            [

                ("↙️ Низ слева","bl"),

                ("⬇️ Низ центр","bc"),

                ("↘️ Низ справа","br")

            ]

        ]



        from telegram import (
            InlineKeyboardButton,
            InlineKeyboardMarkup
        )


        buttons = []


        for row in keyboard:

            buttons.append(

                [

                    InlineKeyboardButton(

                        text,

                        callback_data=
                        "wm_pos_"+value

                    )

                    for text,value in row

                ]

            )


        await query.message.reply_text(

            "📍 Выберите положение:",

            reply_markup=
            InlineKeyboardMarkup(
                buttons
            )

        )


        return





    # ==========================
    # POSITION SELECT
    # ==========================

    if data.startswith(
        "wm_pos_"
    ):


        position = data.replace(
            "wm_pos_",
            ""
        )


        set_state(

            user_id,

            "position",

            position

        )


        await query.message.reply_text(

            "✅ Положение сохранено"

        )


        return





    # ==========================
    # OPACITY
    # ==========================

    if data == "wm_opacity":


        from telegram import (
            InlineKeyboardButton,
            InlineKeyboardMarkup
        )


        buttons = [

            [

                InlineKeyboardButton(
                    "30%",
                    callback_data="wm_op_30"
                ),

                InlineKeyboardButton(
                    "60%",
                    callback_data="wm_op_60"
                ),

                InlineKeyboardButton(
                    "90%",
                    callback_data="wm_op_90"
                )

            ]

        ]


        await query.message.reply_text(

            "🌫 Прозрачность:",

            reply_markup=
            InlineKeyboardMarkup(
                buttons
            )

        )


        return





    if data.startswith(
        "wm_op_"
    ):


        opacity = int(

            data.replace(
                "wm_op_",
                ""
            )

        )


        # перевод процентов в alpha

        set_state(

            user_id,

            "opacity",

            int(
                opacity*2.55
            )

        )


        await query.message.reply_text(

            "✅ Прозрачность изменена"

        )


        return





    # ==========================
    # UNKNOWN
    # ==========================


    await query.message.reply_text(

        "❌ Функция пока не подключена\n"
        f"Код: {data}"

    )
