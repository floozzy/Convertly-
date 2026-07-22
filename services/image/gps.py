from PIL import Image, ExifTags


def convert_coordinate(value):

    try:

        degrees = (
            float(value[0][0])
            /
            float(value[0][1])
        )

        minutes = (
            float(value[1][0])
            /
            float(value[1][1])
        )

        seconds = (
            float(value[2][0])
            /
            float(value[2][1])
        )


        return round(
            degrees
            +
            minutes / 60
            +
            seconds / 3600,
            6
        )

    except:

        return None



def get_gps_info(path):

    image = Image.open(
        path
    )


    exif = image.getexif()


    if not exif:

        return None



    gps_data = {}


    gps_tag = None


    for key in exif:

        tag = ExifTags.TAGS.get(
            key
        )

        if tag == "GPSInfo":

            gps_tag = exif[key]

            break



    if not gps_tag:

        return None



    for key, value in gps_tag.items():

        name = ExifTags.GPSTAGS.get(
            key,
            key
        )

        gps_data[name] = value



    latitude = gps_data.get(
        "GPSLatitude"
    )


    longitude = gps_data.get(
        "GPSLongitude"
    )


    if not latitude or not longitude:

        return None



    lat = convert_coordinate(
        latitude
    )

    lon = convert_coordinate(
        longitude
    )


    if gps_data.get(
        "GPSLatitudeRef"
    ) == "S":

        lat = -lat


    if gps_data.get(
        "GPSLongitudeRef"
    ) == "W":

        lon = -lon



    result = {

        "latitude":

            lat,


        "longitude":

            lon,


        "maps":

            f"https://maps.google.com/?q={lat},{lon}"

    }



    altitude = gps_data.get(
        "GPSAltitude"
    )


    if altitude:

        try:

            result["altitude"] = round(
                float(
                    altitude[0]
                )
                /
                float(
                    altitude[1]
                ),
                1
            )

        except:

            pass



    return result
