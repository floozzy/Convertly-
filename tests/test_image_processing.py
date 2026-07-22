from io import BytesIO

from PIL import Image

from app.services.image_processing import process_photo_bytes


def test_process_photo_bytes_grayscale_returns_bytes() -> None:
    image = Image.new("RGB", (10, 10), color=(255, 0, 0))
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    payload = buffer.getvalue()

    result = process_photo_bytes(payload, "grayscale")

    assert result
    assert result.startswith(b"\x89PNG")


def test_process_photo_bytes_resize_returns_bytes() -> None:
    image = Image.new("RGB", (20, 10), color=(0, 255, 0))
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    payload = buffer.getvalue()

    result = process_photo_bytes(payload, "resize")

    assert result
    assert result.startswith(b"\x89PNG")
