import requests



def get_location(latitude, longitude):

    try:

        url = (
            "https://nominatim.openstreetmap.org/reverse"
        )


        params = {

            "lat":
                latitude,

            "lon":
                longitude,

            "format":
                "json",

            "zoom":
                18,

            "accept-language":
                "ru"

        }


        headers = {

            "User-Agent":
                "ConvertlyBot/1.0"

        }


        response = requests.get(

            url,

            params=params,

            headers=headers,

            timeout=10

        )


        if response.status_code != 200:

            return None



        data = response.json()



        address = data.get(
            "address",
            {}
        )



        return {


            "country":

                address.get(
                    "country",
                    "Неизвестно"
                ),



            "city":

                address.get(
                    "city",

                    address.get(
                        "town",

                        address.get(
                            "village",
                            "Неизвестно"
                        )

                    )

                ),



            "region":

                address.get(
                    "state",
                    "Неизвестно"
                ),



            "district":

                address.get(
                    "county",
                    "Неизвестно"
                ),



            "road":

                address.get(
                    "road",
                    "Неизвестно"
                ),



            "display":

                data.get(
                    "display_name",
                    ""
                )

        }



    except Exception:

        return None
