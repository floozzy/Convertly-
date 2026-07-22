from PIL import Image
from pathlib import Path


def compress_image(
    input_path,
    quality=60
):

    path = Path(input_path)

    image = Image.open(path)

    output = path.with_name(
        path.stem + "_compressed.jpg"
    )

    image = image.convert(
        "RGB"
    )

    image.save(
        output,
        optimize=True,
        quality=quality
    )

    return str(output)
