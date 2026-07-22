from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from services.image.watermark import add_watermark

from handlers.image_actions import get_last_image

from utils.state import (
    set_state,
    get_state,
    clear_state
)



async def watermark_action(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id


    set_state(
        user_id,
        "text",
        "© Convertly"
    )


    set_state(
        user_id,
        "color",
        (255,255,255)
    )


    set_state(
        user_id,
        "opacity",
        120
    )


    set_state(
        user_id,
        "size",
        60
    )


    set_state(
        user_id,
        "position",
        "br"
    )



    keyboard = [

        [

            InlineKeyboardButton(
                "✏️ Изменить текст",
                callback_data="wm_text"
            )

        ],

        [

            InlineKeyboardButton(
                "🎨 Цвет",
                callback_data="wm_color"
            ),

            InlineKeyboardButton(
                "🌫 Прозрачность",
                callback_data="wm_opacity"
            )

        ],

        [

            InlineKeyboardButton(
                "📏 Размер",
                callback_data="wm_size"
            ),

            InlineKeyboardButton(
                "📍 Положение",
                callback_data="wm_position"
            )

        ],

        [

            InlineKeyboardButton(
                "✅ Создать",
                callback_data="wm_apply"
            )

        ]

    ]


    await query.message.reply_text(

        "💧 <b>Watermark Studio</b>\n\n"
        "Настройте водяной знак:",

        reply_markup=InlineKeyboardMarkup(
            keyboard
        ),

        parse_mode="HTML"

    )





async def watermark_apply(
    update,
    context
):

    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id


    path = get_last_image(
        user_id
    )


    if not path:


        await query.message.reply_text(

            "❌ Фото не найдено"

        )

        return



    result = add_watermark(

        path,

        get_state(
            user_id,
            "text"
        ),

        get_state(
            user_id,
            "position"
        ),

        get_state(
            user_id,
            "color"
        ),

        get_state(
            user_id,
            "opacity"
        ),

        get_state(
            user_id,
            "size"
        )

    )



    if result:


        with open(
            result,
            "rb"
        ) as file:


            await query.message.reply_document(

                file,

                caption="💧 Watermark готов"

            )



    clear_state(
        user_id
    )
