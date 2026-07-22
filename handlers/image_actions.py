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
        if f.startswith(str(user_id))
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


    data = image_info(
        path
    )


    text = (
        "📊 <b>Image Inspector Pro</b>\n\n"

        f"📄 Файл: {data['name']}\n"
        f"🖼 Формат: {data['format']}\n"
        f"🎨 Цветовой режим: {data['mode']}\n\n"

        f"📐 Размер: "
        f"{data['width']} × {data['height']}\n"

        f"🔢 Пикселей: "
        f"{data['pixels']:,}\n"

        f"📏 Соотношение: "
        f"{data['ratio']}\n"

        f"💾 Вес: "
        f"{data['size_mb']} MB\n\n"

        f"📷 DPI: "
        f"{data['dpi']}\n"

        f"🎨 ICC профиль: "
        f"{'Есть' if data['icc'] else 'Нет'}\n"
    )


    if "gps" in data:

        text += (

            "\n🌍 GPS найден:\n"

            f"Широта: "
            f"{data['gps']['latitude']}\n"

            f"Долгота: "
            f"{data['gps']['longitude']}\n\n"

            "🗺 Карта:\n"

            f"https://maps.google.com/?q="
            f"{data['gps']['latitude']},"
            f"{data['gps']['longitude']}"

        )


    await query.message.reply_text(
        text,
        parse_mode="HTML"
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
