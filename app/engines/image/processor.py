from __future__ import annotations

from typing import Callable

from PIL import Image, ImageFilter


OperationHandler = Callable[[Image.Image], Image.Image]


def available_operations() -> list[str]:
    return ["grayscale", "blur", "resize"]


def apply_image_operation(image: Image.Image, operation: str) -> Image.Image:
    if operation == "grayscale":
        return image.convert("L").convert("RGB")
    if operation == "blur":
        return image.filter(ImageFilter.GaussianBlur(radius=2))
    if operation == "resize":
        return image.resize((image.width // 2, image.height // 2))
    raise ValueError(f"Unsupported operation: {operation}")
