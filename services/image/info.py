from PIL import Image, ExifTags
from pathlib import Path
import os


def convert_gps(value):

    try:

        d = float(value[0][0]) / float(value[0][1])
        m = float(value[1][0]) / float(value[1][1])
        s = float(value[2][0]) / float(value[2][1])

        return d + (m / 60) + (s / 3600)

    except:

        return None



def get_gps(exif):

    gps_info = {}

    for key, value in exif.items():

        name = ExifTags.GPSTAGS.get(
            key,
            key
        )

        gps_info[name] = value


    if not gps_info:
        return None


    lat = gps_info.get(
        "GPSLatitude"
    )

    lon = gps_info.get(
        "GPSLongitude"
    )


    if lat and lon:

        latitude = convert_gps(lat)
        longitude = convert_gps(lon)

        return {
            "latitude": latitude,
            "longitude": longitude
        }


    return None



def image_info(path):

    image = Image.open(path)

    file_size = round(
        os.path.getsize(path)
        /
        1024
        /
        1024,
        2
    )


    width, height = image.size


    pixels = width * height


    ratio = round(
        width / height,
        2
    )


    data = {

        "name":
            Path(path).name,

        "format":
            image.format,

        "mode":
            image.mode,

        "size_mb":
            file_size,

        "width":
            width,

        "height":
            height,

        "pixels":
            pixels,

        "ratio":
            ratio,

        "dpi":
            image.info.get(
                "dpi"
            ),

        "icc":
            bool(
                image.info.get(
                    "icc_profile"
                )
            ),

        "exif":
            {}

    }


    exif_raw = image.getexif()


    for key, value in exif_raw.items():

        tag = ExifTags.TAGS.get(
            key,
            key
        )

        data["exif"][tag] = str(
            value
        )


    gps = get_gps(
        exif_raw
    )


    if gps:

        data["gps"] = gps


    return data
