from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


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


    user_id = query.from_user.id



    print(
        "BUTTON PRESSED:",
        data
    )





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


    if data == "img_watermark":


        await watermark_action(

            update,

            context

        )

        return





    # ==========================
    # WATERMARK APPLY
    # ==========================


    if data == "wm_apply":


        await watermark_apply(

            update,

            context

        )

        return





    # ==========================
    # WATERMARK TEXT
    # ==========================


    if data == "wm_text":


        set_state(

            user_id,

            "waiting_watermark_text",

            True

        )


        await query.message.reply_text(

            "✏️ Введите текст водяного знака:"

        )


        return





    # ==========================
    # WATERMARK POSITION
    # ==========================


    if data == "wm_position":



        keyboard = [


            [

                InlineKeyboardButton(

                    "↖️",

                    callback_data="wm_pos_tl"

                ),

                InlineKeyboardButton(

                    "⬆️",

                    callback_data="wm_pos_tc"

                ),

                InlineKeyboardButton(

                    "↗️",

                    callback_data="wm_pos_tr"

                )

            ],


            [

                InlineKeyboardButton(

                    "🎯 Центр",

                    callback_data="wm_pos_c"

                )

            ],


            [

                InlineKeyboardButton(

                    "↙️",

                    callback_data="wm_pos_bl"

                ),

                InlineKeyboardButton(

                    "⬇️",

                    callback_data="wm_pos_bc"

                ),

                InlineKeyboardButton(

                    "↘️",

                    callback_data="wm_pos_br"

                )

            ]

        ]



        await query.message.reply_text(

            "📍 Выберите положение:",

            reply_markup=InlineKeyboardMarkup(

                keyboard

            )

        )


        return





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


        keyboard = [


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

            "🌫 Выберите прозрачность:",

            reply_markup=InlineKeyboardMarkup(

                keyboard

            )

        )


        return





    if data.startswith(

        "wm_op_"

    ):


        value = int(

            data.replace(

                "wm_op_",

                ""

            )

        )


        set_state(

            user_id,

            "opacity",

            int(value * 2.55)

        )


        await query.message.reply_text(

            "✅ Прозрачность изменена"

        )


        return





    # ==========================
    # UNKNOWN
    # ==========================



    await query.message.reply_text(

        "❌ Функция ещё не подключена\n\n"

        f"Код: {data}"

    )
