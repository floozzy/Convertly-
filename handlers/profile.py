from telegram import Update
from telegram.ext import ContextTypes

from database.users import get_user
from database.history import total_operations
from database.purchases import total_spent


async def profile_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    telegram_id = update.effective_user.id

    user = get_user(telegram_id)

    if user is None:

        await update.message.reply_text(
            "❌ Пользователь не найден."
        )

        return


    premium = "👑 Premium" if user[4] else "🆓 Free"

    stars = user[5]

    files = user[6]

    operations = total_operations(
        telegram_id
    )

    spent = total_spent(
        telegram_id
    )

    created = user[7]


    text = (
        "👤 Ваш профиль\n\n"
        f"🆔 ID: {telegram_id}\n"
        f"🙍 Имя: {user[3]}\n"
        f"📛 Username: @{user[2] if user[2] else '-'}\n\n"
        f"{premium}\n"
        f"⭐ Stars: {stars}\n\n"
        f"📂 Обработано файлов: {files}\n"
        f"📜 Всего операций: {operations}\n"
        f"💸 Потрачено Stars: {spent}\n\n"
        f"📅 Регистрация:\n{created}"
    )

    await update.message.reply_text(text)
