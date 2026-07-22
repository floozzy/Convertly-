from PIL import Image
import os


def convert_to_png(input_path):

    output_path = input_path.rsplit(".", 1)[0] + ".png"

    image = Image.open(input_path)

    image.save(
        output_path,
        "PNG"
    )

    return output_path
