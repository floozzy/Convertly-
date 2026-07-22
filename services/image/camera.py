from PIL import Image, ExifTags



def get_camera_info(path):

    image = Image.open(
        path
    )


    exif = image.getexif()


    if not exif:

        return None



    data = {}


    for key, value in exif.items():

        tag = ExifTags.TAGS.get(
            key,
            key
        )


        data[tag] = value



    camera = {


        "maker":

            data.get(
                "Make",
                "Неизвестно"
            ),


        "model":

            data.get(
                "Model",
                "Неизвестно"
            ),


        "lens":

            data.get(
                "LensModel",
                "Неизвестно"
            ),


        "date":

            data.get(
                "DateTimeOriginal",
                "Неизвестно"
            ),


        "iso":

            data.get(
                "ISOSpeedRatings",
                "Неизвестно"
            ),


        "aperture":

            data.get(
                "FNumber",
                "Неизвестно"
            ),


        "shutter":

            data.get(
                "ExposureTime",
                "Неизвестно"
            ),


        "focal":

            data.get(
                "FocalLength",
                "Неизвестно"
            ),


        "flash":

            data.get(
                "Flash",
                "Неизвестно"
            ),


        "white_balance":

            data.get(
                "WhiteBalance",
                "Неизвестно"
            ),


        "exposure_mode":

            data.get(
                "ExposureMode",
                "Неизвестно"
            ),


        "scene":

            data.get(
                "SceneCaptureType",
                "Неизвестно"
            )

    }


    return camera
