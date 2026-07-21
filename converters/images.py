from PIL import Image
import os


def convert_image(path, fmt):
    img = Image.open(path)

    name = os.path.splitext(path)[0]

    output = f"{name}.{fmt.lower()}"

    if fmt.lower() == "jpg":
        img = img.convert("RGB")

    img.save(output)

    return output


def compress_image(path):
    img = Image.open(path)

    output = "compressed.jpg"

    img.convert("RGB").save(
        output,
        quality=35,
        optimize=True
    )

    return output

