from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import ContextTypes


from services.image.watermark import add_watermark


from utils.images import get_image


from utils.state import (
    set_state,
    get_state,
    clear_state
)





# =====================================
# OPEN WATERMARK MENU
# =====================================


async def watermark_action(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):


    query = update.callback_query


    await query.answer()



    user_id = query.from_user.id



    # default settings


    if not get_state(
        user_id,
        "text"
    ):


        set_state(

            user_id,

            "text",

            "© Convertly"

        )


    if not get_state(
        user_id,
        "color"
    ):


        set_state(

            user_id,

            "color",

            (255,255,255)

        )


    if not get_state(
        user_id,
        "opacity"
    ):


        set_state(

            user_id,

            "opacity",

            180

        )


    if not get_state(
        user_id,
        "size"
    ):


        set_state(

            user_id,

            "size",

            80

        )


    if not get_state(
        user_id,
        "position"
    ):


        set_state(

            user_id,

            "position",

            "br"

        )




    keyboard = [


        [

            InlineKeyboardButton(

                "✏️ Текст",

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
        f"Текст: {get_state(user_id,'text')}\n"
        f"Размер: {get_state(user_id,'size')}\n"
        f"Позиция: {get_state(user_id,'position')}",

        reply_markup=InlineKeyboardMarkup(
            keyboard
        ),

        parse_mode="HTML"

    )






# =====================================
# APPLY WATERMARK
# =====================================



async def watermark_apply(

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

            "❌ Фото не найдено.\n"
            "Сначала отправьте изображение."

        )


        return



    try:



        result = add_watermark(

            path,


            get_state(

                user_id,

                "text",

                "© Convertly"

            ),


            get_state(

                user_id,

                "position",

                "br"

            ),


            get_state(

                user_id,

                "color",

                (255,255,255)

            ),


            get_state(

                user_id,

                "opacity",

                180

            ),


            get_state(

                user_id,

                "size",

                80

            )

        )



        if not result:


            await query.message.reply_text(

                "❌ Не удалось создать watermark."

            )


            return




        with open(

            result,

            "rb"

        ) as photo:


            await query.message.reply_photo(

                photo,

                caption="💧 Watermark готов"

            )



    except Exception as e:


        print(

            "WATERMARK ERROR:",

            e

        )


        await query.message.reply_text(

            "❌ Ошибка watermark:\n"

            +


            str(e)

        )




# =====================================
# TEXT INPUT MODE
# =====================================



async def watermark_text_start(

    update,

    context

):


    user_id = update.effective_user.id



    set_state(

        user_id,

        "waiting_watermark_text",

        True

    )



    await update.message.reply_text(

        "✏️ Отправьте новый текст водяного знака."

    )
