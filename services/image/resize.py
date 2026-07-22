from PIL import Image
from pathlib import Path


def resize_image(
    input_path,
    width,
    height
):

    image = Image.open(input_path)

    output = Path(input_path).with_name(
        Path(input_path).stem + "_resized.jpg"
    )

    image.resize(
        (width, height)
    ).save(output)

    return str(output)
