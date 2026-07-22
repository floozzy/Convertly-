from __future__ import annotations

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def build_main_menu() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton("🖼 Обработать фото", callback_data="action:photo")],
        [InlineKeyboardButton("📄 PDF tools", callback_data="action:pdf")],
        [InlineKeyboardButton("🤖 AI tools", callback_data="action:ai")],
        [InlineKeyboardButton("ℹ️ Помощь", callback_data="action:help")],
    ]
    return InlineKeyboardMarkup(buttons)


def build_photo_menu() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton("⚫ Ч/Б", callback_data="op:grayscale")],
        [InlineKeyboardButton("🌫 Размытие", callback_data="op:blur")],
        [InlineKeyboardButton("📏 Уменьшить", callback_data="op:resize")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="action:main")],
    ]
    return InlineKeyboardMarkup(buttons)
