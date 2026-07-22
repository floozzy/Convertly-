from __future__ import annotations

from io import BytesIO

from PIL import Image


def process_photo_bytes(photo_bytes: bytes, operation: str) -> bytes:
    image = Image.open(BytesIO(photo_bytes)).convert("RGB")

    if operation == "grayscale":
        image = image.convert("L")
    elif operation == "blur":
        image = image.filter(ImageFilter.GaussianBlur(radius=2))
    elif operation == "resize":
        image = image.resize((512, 512))
    else:
        image = image.copy()

    output = BytesIO()
    image.save(output, format="PNG")
    return output.getvalue()
