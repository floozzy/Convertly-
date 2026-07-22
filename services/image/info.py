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

from services.image.camera import (
    get_camera_info
)

from services.image.gps import (
    get_gps_info
)

from services.image.ocr import (
    extract_text
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


        "size_mb":

            round(
                file_size / 1024 / 1024,
                2
            ),



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
            ),



        "quality":

            analyze_quality(
                path
            ),



        "camera":

            get_camera_info(
                path
            ),



        "gps":

            get_gps_info(
                path
            ),



        "ocr":

            extract_text(
                path
            )

    }
