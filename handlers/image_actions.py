import os

from telegram.ext import ContextTypes

from services.image.compress import compress_image
from services.image.convert import convert_image
from services.image.info import image_info

from database.history import add_history


UPLOAD_DIR = "files/uploads"



def get_last_image(user_id):

    files = [

        f
        for f in os.listdir(UPLOAD_DIR)

        if f.startswith(
            str(user_id)
        )

    ]


    if not files:

        return None


    return os.path.join(
        UPLOAD_DIR,
        files[-1]
    )



async def image_compress_action(
    update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id


    path = get_last_image(
        user_id
    )


    if not path:

        await query.message.reply_text(
            "❌ Фото не найдено."
        )

        return



    await query.message.reply_text(
        "📦 Сжимаю изображение..."
    )


    result = compress_image(
        path
    )


    add_history(
        user_id,
        path,
        "Сжатие изображения"
    )


    with open(
        result,
        "rb"
    ) as file:

        await query.message.reply_document(
            document=file,
            caption="✅ Изображение сжато"
        )



async def image_convert_action(
    update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id


    path = get_last_image(
        user_id
    )


    if not path:

        await query.message.reply_text(
            "❌ Фото не найдено."
        )

        return



    await query.message.reply_text(
        "🔄 Конвертирую JPG → PNG..."
    )


    result = convert_image(
        path,
        "png"
    )


    add_history(
        user_id,
        path,
        "JPG → PNG"
    )


    with open(
        result,
        "rb"
    ) as file:

        await query.message.reply_document(
            document=file,
            caption="✅ JPG → PNG готово"
        )



async def image_info_action(
    update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id


    path = get_last_image(
        user_id
    )


    if not path:

        await query.message.reply_text(
            "❌ Фото не найдено."
        )

        return



    await query.message.reply_text(
        "🔍 Анализирую изображение..."
    )



    data = image_info(
        path
    )


    colors = data["colors"]


    text = (

        "📊 <b>Image Inspector Pro</b>\n\n"


        "🗂 <b>Файл</b>\n"

        f"📄 {data['name']}\n"

        f"🖼 Формат: {data['format']}\n"

        f"🎨 Режим: {data['mode']}\n"

        f"💾 Размер: {data['size_mb']} MB\n\n"



        "📐 <b>Изображение</b>\n"

        f"Ширина: {data['width']} px\n"

        f"Высота: {data['height']} px\n"

        f"Пикселей: {data['pixels']:,}\n"

        f"Соотношение: {data['ratio']}\n\n"



        "🎨 <b>Цветовой анализ</b>\n"

        f"Средний цвет: {colors['average_color']}\n"

        f"☀ Яркость: {colors['brightness']}\n"

        f"◼ Контраст: {colors['contrast']}\n"

        f"🌈 Насыщенность: {colors['saturation']}\n\n"



        "🎨 <b>Популярные цвета:</b>\n"

    )



    for color in colors["popular_colors"]:

        text += (

            f"{color['hex']} — "
            f"{color['percent']}%\n"

        )



    text += "\n🔐 <b>Хэши</b>\n"

    text += (

        f"MD5:\n"
        f"<code>{data['hashes']['md5']}</code>\n\n"

        f"SHA1:\n"
        f"<code>{data['hashes']['sha1']}</code>\n\n"

        f"SHA256:\n"
        f"<code>{data['hashes']['sha256']}</code>\n\n"

    )



    text += (

        "🕒 <b>Даты</b>\n"

        f"Создан: {data['dates']['created']}\n"

        f"Изменён: {data['dates']['modified']}\n\n"

    )



    exif = data["metadata"]["exif"]


    if exif:

        text += "📷 <b>EXIF найден:</b>\n"


        count = 0


        for key, value in exif.items():

            text += (
                f"{key}: {value}\n"
            )

            count += 1


            if count >= 15:

                text += (
                    "...и другие данные"
                )

                break


    else:

        text += (
            "📷 EXIF: отсутствует\n"
        )



    await query.message.reply_text(

        text,

        parse_mode="HTML"

    )
