data = image_info(path)


text = (
    "📊 <b>Image Inspector Pro</b>\n\n"

    f"📄 Файл: {data['name']}\n"
    f"🖼 Формат: {data['format']}\n"
    f"🎨 Цветовой режим: {data['mode']}\n\n"

    f"📐 Размер: {data['width']} × {data['height']}\n"
    f"🔢 Пикселей: {data['pixels']:,}\n"
    f"📏 Соотношение: {data['ratio']}\n"
    f"💾 Вес: {data['size_mb']} MB\n\n"

    f"📷 DPI: {data['dpi']}\n"
    f"🎨 ICC профиль: {'Есть' if data['icc'] else 'Нет'}\n"
)


if "gps" in data:

    text += (
        "\n🌍 GPS найден:\n"
        f"Широта: {data['gps']['latitude']}\n"
        f"Долгота: {data['gps']['longitude']}\n\n"

        f"🗺 Карта:\n"
        f"https://maps.google.com/?q="
        f"{data['gps']['latitude']},"
        f"{data['gps']['longitude']}"
    )


await query.message.reply_text(
    text,
    parse_mode="HTML"
)
