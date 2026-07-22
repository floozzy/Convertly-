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


from services.image.faces import (
    detect_faces
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


        # =====================
        # FILE
        # =====================

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



        # =====================
        # IMAGE
        # =====================

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



        # =====================
        # HASHES
        # =====================

        "hashes":

            calculate_hashes(
                path
            ),



        # =====================
        # DATES
        # =====================

        "dates":

            get_file_dates(
                path
            ),



        # =====================
        # METADATA
        # =====================

        "metadata":

            get_metadata(
                path
            ),



        # =====================
        # COLORS
        # =====================

        "colors":

            analyze_colors(
                path
            ),



        # =====================
        # QUALITY
        # =====================

        "quality":

            analyze_quality(
                path
            ),



        # =====================
        # CAMERA
        # =====================

        "camera":

            get_camera_info(
                path
            ),



        # =====================
        # GPS
        # =====================

        "gps":

            get_gps_info(
                path
            ),



        # =====================
        # OCR
        # =====================

        "ocr":

            extract_text(
                path
            ),



        # =====================
        # FACES
        # =====================

        "faces":

            detect_faces(
                path
            )

    }
