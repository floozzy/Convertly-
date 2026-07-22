from PIL import Image, ImageStat
from collections import Counter


def rgb_to_hex(rgb):

    return "#{:02x}{:02x}{:02x}".format(
        int(rgb[0]),
        int(rgb[1]),
        int(rgb[2])
    ).upper()



def analyze_colors(path):

    image = Image.open(
        path
    ).convert(
        "RGB"
    )


    # уменьшаем для ускорения анализа

    small = image.resize(
        (100, 100)
    )


    pixels = list(
        small.getdata()
    )


    # средний цвет

    avg = tuple(
        sum(
            pixel[i]
            for pixel in pixels
        )
        /
        len(pixels)

        for i in range(3)
    )


    # популярные цвета

    counter = Counter(
        pixels
    )


    popular = []


    for color, count in counter.most_common(5):

        popular.append(
            {
                "hex":
                    rgb_to_hex(color),

                "percent":
                    round(
                        count /
                        len(pixels)
                        *
                        100,
                        1
                    )
            }
        )


    stat = ImageStat.Stat(
        image
    )


    # яркость

    brightness = sum(
        stat.mean
    ) / 3


    # контраст

    contrast = sum(
        stat.stddev
    ) / 3


    # насыщенность через HSV

    hsv = image.convert(
        "HSV"
    )

    hsv_stat = ImageStat.Stat(
        hsv
    )

    saturation = hsv_stat.mean[1]


    return {

        "average_color":

            rgb_to_hex(
                avg
            ),


        "brightness":

            round(
                brightness,
                1
            ),


        "contrast":

            round(
                contrast,
                1
            ),


        "saturation":

            round(
                saturation,
                1
            ),


        "popular_colors":

            popular

    }
