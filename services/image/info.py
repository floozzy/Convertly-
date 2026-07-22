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

from services.image.quality import (
    analyze_quality
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


        # Файл

        "name":

            Path(path).name,


        "format":

            image.format,


        "mode":

            image.mode,


        "size_mb":

            round(
                file_size / 1024 / 1024,
                2
            ),



        # Размеры

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



        # Хэши

        "hashes":

            calculate_hashes(
                path
            ),



        # Даты

        "dates":

            get_file_dates(
                path
            ),



        # EXIF + Metadata

        "metadata":

            get_metadata(
                path
            ),



        # Цвет

        "colors":

            analyze_colors(
                path
            ),



        # Качество

        "quality":

            analyze_quality(
                path
            )

    }
