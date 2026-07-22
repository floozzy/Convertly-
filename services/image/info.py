from PIL import Image
from pathlib import Path
import os


def image_info(
    path
):

    image = Image.open(path)


    return {

        "name":
            Path(path).name,

        "format":
            image.format,

        "width":
            image.width,

        "height":
            image.height,

        "size":
            round(
                os.path.getsize(path)
                /
                1024
                /
                1024,
                2
            )

    }
