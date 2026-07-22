from PIL import Image, ExifTags

from services.image.location import get_location



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



    gps = None


    for key in exif:

        tag = ExifTags.TAGS.get(
            key
        )


        if tag == "GPSInfo":

            gps = exif[key]

            break



    if not gps:

        return None



    gps_data = {}


    for key, value in gps.items():

        name = ExifTags.GPSTAGS.get(
            key,
            key
        )

        gps_data[name] = value



    if not gps_data.get(
        "GPSLatitude"
    ):

        return None



    lat = convert_coordinate(
        gps_data["GPSLatitude"]
    )


    lon = convert_coordinate(
        gps_data["GPSLongitude"]
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



    location = get_location(

        lat,

        lon

    )


    if location:

        result["location"] = location



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
