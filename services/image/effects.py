from PIL import Image, ImageFilter
from pathlib import Path



def grayscale(path):

    image = Image.open(path)

    output = Path(path).with_name(
        Path(path).stem + "_gray.jpg"
    )

    image.convert(
        "L"
    ).save(output)

    return str(output)



def blur(path):

    image = Image.open(path)

    output = Path(path).with_name(
        Path(path).stem + "_blur.jpg"
    )

    image.filter(
        ImageFilter.BLUR
    ).save(output)

    return str(output)



def flip_horizontal(path):

    image = Image.open(path)

    output = Path(path).with_name(
        Path(path).stem + "_flip.jpg"
    )

    image.transpose(
        Image.Transpose.FLIP_LEFT_RIGHT
    ).save(output)

    return str(output)



def flip_vertical(path):

    image = Image.open(path)

    output = Path(path).with_name(
        Path(path).stem + "_flip_v.jpg"
    )

    image.transpose(
        Image.Transpose.FLIP_TOP_BOTTOM
    ).save(output)

    return str(output)



def thumbnail(path):

    image = Image.open(path)

    output = Path(path).with_name(
        Path(path).stem + "_thumb.jpg"
    )

    image.thumbnail(
        (300,300)
    )

    image.save(output)

    return str(output)
