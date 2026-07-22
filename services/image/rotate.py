from PIL import Image
from pathlib import Path


def rotate_image(
    input_path,
    angle
):

    image = Image.open(input_path)

    output = Path(input_path).with_name(
        Path(input_path).stem + "_rotated.jpg"
    )

    image.rotate(
        angle,
        expand=True
    ).save(output)

    return str(output)
