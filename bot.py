import os
import uuid
import asyncio

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)

from converters.images import convert_image, compress_image
from converters.audio import convert_audio


TOKEN = "8831427693:AAED6ZtuPdcZnvsAvku-DPNSZ_QsBNzrc0I"


FILES = "files"

os.makedirs(FILES, exist_ok=True)


users = {}


# =====================
# КОМАНДА START
# =====================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user.id

    users[user] = users.get(user,0)


    keyboard = [

        [
            InlineKeyboardButton(
                "🖼 Изображения",
                callback_data="images"
            )
        ],

        [
            InlineKeyboardButton(
                "🎵 Аудио",
                callback_data="audio"
            )
        ],

        [
            InlineKeyboardButton(
                "🗜 Сжать фото",
                callback_data="compress"
            )
        ],

        [
            InlineKeyboardButton(
                "ℹ️ Информация",
                callback_data="info"
            )
        ]

    ]


    await update.message.reply_text(

        "🚀 Convertly\n\n"
        "Твой личный конвертер файлов.\n\n"
        "Выбери действие:",

        reply_markup=InlineKeyboardMarkup(keyboard)

    )



# =====================
# КНОПКИ
# =====================


async def buttons(update:Update, context):

    query = update.callback_query

    await query.answer()


    if query.data=="images":

        context.user_data["mode"]="images"

        await query.message.reply_text(
            "🖼 Отправь JPG/PNG/WEBP"
        )


    elif query.data=="audio":

        context.user_data["mode"]="audio"

        await query.message.reply_text(
            "🎵 Отправь MP3 или WAV"
        )


    elif query.data=="compress":

        context.user_data["mode"]="compress"

        await query.message.reply_text(
            "🗜 Отправь фото для сжатия"
        )


    elif query.data=="info":

        await query.message.reply_text(

            "Convertly 1.0\n\n"
            "⚡ Работает на твоём телефоне\n"
            "📱 Android Server\n"
            "🐍 Python"

        )



# =====================
# ФАЙЛЫ
# =====================


async def files(update:Update, context):


    mode=context.user_data.get(
        "mode"
    )


    if not mode:

        await update.message.reply_text(
            "Сначала выбери действие через /start"
        )

        return



    tg_file=None


    if update.message.document:

        tg_file=await update.message.document.get_file()


    elif update.message.photo:

        tg_file=await update.message.photo[-1].get_file()


    elif update.message.audio:

        tg_file=await update.message.audio.get_file()



    else:

        return



    filename=f"{FILES}/{uuid.uuid4()}"

    await tg_file.download_to_drive(filename)



    await update.message.reply_text(
        "⚙️ Обрабатываю файл..."
    )


    try:


        result=None


        if mode=="images":

            result=convert_image(
                filename,
                "png"
            )


        elif mode=="compress":

            result=compress_image(
                filename
            )


        elif mode=="audio":

            result=convert_audio(
                filename,
                "wav"
            )



        if result:


            await update.message.reply_document(
                document=open(result,"rb")
            )


        users[update.effective_user.id]+=1



    except Exception as e:


        await update.message.reply_text(
            f"❌ Ошибка:\n{e}"
        )



# =====================
# ЗАПУСК
# =====================


app = Application.builder().token(
    TOKEN
).build()


app.add_handler(
    CommandHandler(
        "start",
        start
    )
)


app.add_handler(
    CallbackQueryHandler(
        buttons
    )
)

app.add_handler(
    MessageHandler(
        filters.ALL,
        files
    )
)


print(
    "🔥 Convertly запущен"
)


app.run_polling()
