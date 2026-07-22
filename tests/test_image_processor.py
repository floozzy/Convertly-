from PIL import Image

from app.engines.image.processor import apply_image_operation, available_operations
from app.services.bot_service import build_help_message, build_start_message


def test_available_operations_include_core_features():
    operations = available_operations()
    assert "grayscale" in operations
    assert "blur" in operations
    assert "resize" in operations


def test_apply_image_operation_returns_image_with_expected_size():
    image = Image.new("RGB", (16, 12), color=(255, 0, 0))
    result = apply_image_operation(image, "grayscale")

    assert result.size == (16, 12)
    assert result.mode == "RGB"


def test_bot_messages_are_descriptive():
    start_message = build_start_message()
    help_message = build_help_message()

    assert "Convertly" in start_message
    assert "/help" in help_message
    assert "/start" in help_message
