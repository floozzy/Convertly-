from PIL import Image
from pathlib import Path
import os

from services.image.hashes import calculate_hashes
from services.image.metadata import (
    get_file_dates,
    get_metadata
)

from services.image.colors import (
    analyze_colors
)



def image_info(path):

    image = Image.open(
        path
    )


    width, height = image.size


    file_size = os.path.getsize(
        path
    )


    return {

        "name":

            Path(path).name,


        "format":

            image.format,


        "mode":

            image.mode,


        "width":

            width,


        "height":

            height,


        "pixels":

            width * height,


        "ratio":

            round(
                width / height,
                2
            ),


        "size_mb":

            round(
                file_size / 1024 / 1024,
                2
            ),


        "hashes":

            calculate_hashes(
                path
            ),


        "dates":

            get_file_dates(
                path
            ),


        "metadata":

            get_metadata(
                path
            ),


        "colors":

            analyze_colors(
                path
            )

    }
