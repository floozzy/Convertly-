from pathlib import Path
from PIL import Image
import os


def image_info(path):

    image = Image.open(path)

    return {

        "name": Path(path).name,

        "width": image.width,

        "height": image.height,

        "format": image.format,

        "size_mb": round(
            os.path.getsize(path) /
            1024 /
            1024,
            2
        )

    }
