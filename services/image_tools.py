from PIL import Image
import os



def rotate_image(path, angle):

    image = Image.open(path)

    image = image.rotate(
        angle,
        expand=True
    )


    output = (
        path.rsplit(".",1)[0]
        + "_rotated.png"
    )


    image.save(output)

    return output




def image_info(path):

    image = Image.open(path)

    return {
        "width": image.width,
        "height": image.height,
        "format": image.format
    }
