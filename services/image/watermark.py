from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


def add_watermark(
    path,
    text="Convertly"
):

    image = Image.open(path).convert(
        "RGBA"
    )

    draw = ImageDraw.Draw(
        image
    )

    draw.text(
        (20,20),
        text,
        fill=(255,255,255,180)
    )


    output = Path(path).with_name(
        Path(path).stem + "_watermark.png"
    )

    image.save(output)

    return str(output)
