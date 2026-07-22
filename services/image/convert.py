from PIL import Image
from pathlib import Path


SUPPORTED = {
    "jpg",
    "jpeg",
    "png",
    "webp",
    "bmp",
    "tiff",
    "ico"
}


def convert_image(
    input_path,
    output_format
):

    path = Path(input_path)

    image = Image.open(path)

    output = path.with_suffix(
        "." + output_format.lower()
    )


    if output_format.lower() in (
        "jpg",
        "jpeg"
    ):

        image = image.convert(
            "RGB"
        )


    image.save(
        output,
        output_format.upper()
    )


    return str(output)
