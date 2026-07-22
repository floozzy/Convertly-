from PIL import Image
from pathlib import Path


def convert_image(
    input_path,
    output_format
):

    image = Image.open(input_path)

    output_format = output_format.lower()

    output_path = Path(input_path).with_suffix(
        "." + output_format
    )


    if output_format in [
        "jpg",
        "jpeg"
    ]:
        image = image.convert(
            "RGB"
        )


    image.save(
        output_path,
        output_format.upper()
    )


    return str(output_path)
