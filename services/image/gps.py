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

    try:

        image = Image.open(
            path
        )


        exif = image.getexif()


        if not exif:

            return None



        gps_raw = None


        # ищем GPSInfo

        for key, value in exif.items():

            tag = ExifTags.TAGS.get(
                key
            )


            if tag == "GPSInfo":

                gps_raw = value

                break



        if gps_raw is None:

            return None



        # Pillow иногда отдаёт число вместо словаря

        if isinstance(
            gps_raw,
            int
        ):

            try:

                gps_raw = exif.get_ifd(
                    gps_raw
                )

            except:

                return None



        if not isinstance(
            gps_raw,
            dict
        ):

            return None



        gps_data = {}



        for key, value in gps_raw.items():

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


        if lat is None or lon is None:

            return None



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



        # город / страна

        location = get_location(
            lat,
            lon
        )


        if location:

            result["location"] = location



        # высота

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



    except Exception:

        return None
