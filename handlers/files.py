import os

from telegram import Update
from telegram.ext import ContextTypes

from services.image_converter import convert_to_png


async def file_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    document = update.message.document

    if not document:
        return


    filename = document.file_name

    await update.message.reply_text(
        "📥 Получил файл!\n"
        f"📄 {filename}\n\n"
        "⚙️ Начинаю обработку..."
    )


    file = await document.get_file()


    input_path = f"files/{filename}"


    await file.download_to_drive(
        input_path
    )


    if filename.lower().endswith(
        (".jpg", ".jpeg", ".webp")
    ):

        output = convert_to_png(
            input_path
        )


        await update.message.reply_document(
            document=open(output, "rb"),
            caption="✅ Готово! Конвертация JPG → PNG"
        )


    else:

        await update.message.reply_text(
            "❌ Пока этот формат не поддерживается."
        )
