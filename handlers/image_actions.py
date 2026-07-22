import os

from telegram.ext import ContextTypes

from services.image.compress import compress_image
from services.image.convert import convert_image
from services.image.info import image_info

from database.history import add_history


UPLOAD_DIR = "files/uploads"



def get_last_image(user_id):

    if not os.path.exists(
        UPLOAD_DIR
    ):
        return None


    files = [

        f
        for f in os.listdir(
            UPLOAD_DIR
        )

        if f.startswith(
            str(user_id)
        )

    ]


    if not files:

        return None


    files.sort(
        key=lambda x: os.path.getmtime(
            os.path.join(
                UPLOAD_DIR,
                x
            )
        )
    )


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


    path = get_last_image(
        query.from_user.id
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
        query.from_user.id,
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


    path = get_last_image(
        query.from_user.id
    )


    if not path:

        await query.message.reply_text(
            "❌ Фото не найдено."
        )

        return



    await query.message.reply_text(
        "🔄 Конвертирую изображение..."
    )


    result = convert_image(
        path,
        "png"
    )


    add_history(
        query.from_user.id,
        path,
        "Конвертация PNG"
    )


    with open(
        result,
        "rb"
    ) as file:


        await query.message.reply_document(
            document=file,
            caption="✅ Конвертация завершена"
        )



async def image_info_action(
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
            "❌ Фото не найдено."
        )

        return



    await query.message.reply_text(
        "🔍 Анализирую изображение..."
    )


    data = image_info(
        path
    )


    text = (
        "📊 <b>Convertly Image Inspector Pro</b>\n\n"
    )


    # FILE

    text += (
        "━━━━━━━━━━━━━━\n"
        "🗂 <b>Файл</b>\n"
        f"📄 {data['name']}\n"
        f"🖼 Формат: {data['format']}\n"
        f"🎨 Режим: {data['mode']}\n"
        f"💾 Размер: {data['size_mb']} MB\n\n"
    )


    # IMAGE

    text += (
        "━━━━━━━━━━━━━━\n"
        "📐 <b>Изображение</b>\n"
        f"↔️ {data['width']} px\n"
        f"↕️ {data['height']} px\n"
        f"🔢 {data['pixels']:,} пикселей\n"
        f"📏 Соотношение: {data['ratio']}\n\n"
    )


    # COLORS

    colors = data.get(
        "colors"
    )


    if colors:

        text += (
            "━━━━━━━━━━━━━━\n"
            "🎨 <b>Цветовой анализ</b>\n"
            f"Средний цвет: {colors['average_color']}\n"
            f"☀ Яркость: {colors['brightness']}\n"
            f"◼ Контраст: {colors['contrast']}\n"
            f"🌈 Насыщенность: {colors['saturation']}\n\n"
        )


        text += "🎨 Топ цветов:\n"


        for color in colors["popular_colors"]:

            text += (
                f"{color['hex']} — "
                f"{color['percent']}%\n"
            )


    # QUALITY

    quality = data.get(
        "quality"
    )


    if quality:

        text += (
            "\n━━━━━━━━━━━━━━\n"
            "🧠 <b>Качество</b>\n"
            f"⭐ {quality['score']}/100\n"
            f"{quality['verdict']}\n"
            f"🔍 Резкость: {quality['sharpness']}\n"
            f"☀ Свет: {quality['light_status']}\n"
            f"🌫 Шум: {quality['noise']}\n\n"
        )



    # CAMERA

    camera = data.get(
        "camera"
    )


    if camera:


        text += (
            "━━━━━━━━━━━━━━\n"
            "📷 <b>Камера</b>\n"
            f"🏭 Производитель: {camera['maker']}\n"
            f"📱 Модель: {camera['model']}\n"
            f"🔭 Объектив: {camera['lens']}\n"
            f"ISO: {camera['iso']}\n"
            f"Выдержка: {camera['shutter']}\n"
            f"Диафрагма: {camera['aperture']}\n"
            f"Фокус: {camera['focal']}\n\n"
        )



    # GPS

    gps = data.get(
        "gps"
    )


    if gps:


        text += (
            "━━━━━━━━━━━━━━\n"
            "🌍 <b>GPS Intelligence</b>\n"
            f"📍 {gps['latitude']}, {gps['longitude']}\n"
        )


        if "altitude" in gps:

            text += (
                f"⛰ Высота: {gps['altitude']} м\n"
            )


        if "location" in gps:


            loc = gps["location"]


            text += (
                "\n🏙 <b>Место:</b>\n"
                f"🌎 {loc['country']}\n"
                f"🏙 {loc['city']}\n"
                f"📌 {loc['district']}\n"
                f"🛣 {loc['road']}\n"
            )


        text += (
            "\n🗺 Карта:\n"
            f"{gps['maps']}\n"
        )



    else:

        text += (
            "\n━━━━━━━━━━━━━━\n"
            "🌍 GPS: отсутствует\n"
        )



    # HASHES

    hashes = data.get(
        "hashes"
    )


    if hashes:


        text += (
            "\n━━━━━━━━━━━━━━\n"
            "🔐 <b>Хэши</b>\n"
            f"MD5:\n<code>{hashes['md5']}</code>\n\n"
            f"SHA256:\n<code>{hashes['sha256']}</code>\n"
        )



    await query.message.reply_text(
        text,
        parse_mode="HTML"
        )
