from PIL import Image
import os


def convert_image(
    input_path,
    output_format
):

    image = Image.open(input_path)

    output_path = (
        input_path.rsplit(".", 1)[0]
        + "."
        + output_format.lower()
    )


    if output_format.lower() == "jpg":
        image = image.convert("RGB")


    image.save(
        output_path,
        output_format.upper()
    )

    return output_path



def compress_image(
    input_path,
    quality=60
):

    image = Image.open(input_path)

    output_path = (
        input_path.rsplit(".", 1)[0]
        + "_compressed.jpg"
    )


    image.convert(
        "RGB"
    ).save(
        output_path,
        "JPEG",
        quality=quality
    )


    return output_path



def resize_image(
    input_path,
    width,
    height
):

    image = Image.open(input_path)

    image = image.resize(
        (
            width,
            height
        )
    )


    output_path = (
        input_path.rsplit(".",1)[0]
        + "_resized.png"
    )


    image.save(
        output_path
    )


    return output_path
