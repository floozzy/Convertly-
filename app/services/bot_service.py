from __future__ import annotations


def build_start_message() -> str:
    return (
        "Welcome to Convertly!\n"
        "Send me an image and I will transform it with built-in tools."
    )


def build_help_message() -> str:
    return (
        "Available commands:\n"
        "/start - show welcome message\n"
        "/help - show this message\n"
        "Send an image for processing."
    )
