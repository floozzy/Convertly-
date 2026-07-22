from PIL import Image, ExifTags
from datetime import datetime
import os


def get_file_dates(path):

    created = os.path.getctime(
        path
    )

    modified = os.path.getmtime(
        path
    )


    return {

        "created":

            datetime.fromtimestamp(
                created
            ).strftime(
                "%d.%m.%Y %H:%M:%S"
            ),


        "modified":

            datetime.fromtimestamp(
                modified
            ).strftime(
                "%d.%m.%Y %H:%M:%S"
            )

    }



def get_metadata(path):

    image = Image.open(
        path
    )


    result = {

        "format":
            image.format,


        "mode":
            image.mode,


        "info":
            {}

    }


    # обычные метаданные PIL

    for key, value in image.info.items():

        try:

            result["info"][key] = str(
                value
            )

        except:

            pass



    # EXIF

    exif = image.getexif()


    result["exif"] = {}


    for key, value in exif.items():

        tag = ExifTags.TAGS.get(
            key,
            key
        )


        result["exif"][tag] = str(
            value
        )


    return result
