from PIL import Image, ImageFilter, ImageStat
import numpy as np



def analyze_quality(path):

    image = Image.open(
        path
    ).convert(
        "L"
    )


    # Резкость через разницу с размытой копией

    blurred = image.filter(
        ImageFilter.GaussianBlur(
            radius=5
        )
    )


    original = np.array(
        image,
        dtype=float
    )


    blur_array = np.array(
        blurred,
        dtype=float
    )


    sharpness = np.mean(
        np.abs(
            original - blur_array
        )
    )


    sharpness_score = min(
        round(
            sharpness * 5,
            1
        ),
        100
    )



    # Яркость

    stat = ImageStat.Stat(
        image
    )


    brightness = stat.mean[0]


    if brightness < 40:

        light_status = "Очень тёмное 🌑"


    elif brightness > 210:

        light_status = "Очень светлое ☀️"


    else:

        light_status = "Нормальное"



    # Контраст

    contrast = stat.stddev[0]



    # Оценка шума

    edges = image.filter(
        ImageFilter.FIND_EDGES
    )


    noise_stat = ImageStat.Stat(
        edges
    )


    noise = noise_stat.mean[0]


    if noise > 25:

        noise_level = "Высокий"

    elif noise > 10:

        noise_level = "Средний"

    else:

        noise_level = "Низкий"



    # Общая оценка

    score = (

        sharpness_score * 0.5

        +

        min(
            contrast * 2,
            100
        ) * 0.3

        +

        (100 - min(noise,100))
        *0.2

    )


    score = round(
        score,
        1
    )


    if score >= 80:

        verdict = "🔥 Отличное качество"

    elif score >= 60:

        verdict = "👍 Хорошее качество"

    elif score >= 40:

        verdict = "👌 Среднее качество"

    else:

        verdict = "⚠️ Низкое качество"



    return {


        "score":
            score,


        "verdict":
            verdict,


        "sharpness":
            sharpness_score,


        "brightness":
            round(
                brightness,
                1
            ),


        "light_status":
            light_status,


        "contrast":
            round(
                contrast,
                1
            ),


        "noise":
            noise_level

  }
