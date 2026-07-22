from telegram import Update
from telegram.ext import ContextTypes

from services.user_service import UserService


async def profile_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id

    profile = UserService.profile(
        user_id
    )

    if profile is None:

        await update.message.reply_text(
            "❌ Профиль не найден.\n"
            "Нажмите /start"
        )

        return


    status = (
        "👑 Premium"
        if profile["premium"]
        else
        "🆓 Free"
    )


    username = (
        f"@{profile['username']}"
        if profile["username"]
        else
        "нет"
    )


    text = (
        "👤 <b>Ваш профиль Convertly</b>\n\n"

        f"🆔 ID: <code>{profile['telegram_id']}</code>\n"
        f"🙍 Имя: {profile['first_name']}\n"
        f"📛 Username: {username}\n\n"

        f"📌 Статус: {status}\n"
        f"⭐ Stars: {profile['stars']}\n\n"

        f"📂 Файлов обработано: {profile['files']}\n"
        f"📜 Операций: {profile['operations']}\n"
        f"💸 Потрачено Stars: {profile['spent']}\n\n"

        f"📅 Регистрация:\n"
        f"{profile['created']}"
    )


    await update.message.reply_text(
        text,
        parse_mode="HTML"
    )
