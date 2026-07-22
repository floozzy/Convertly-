from PIL import Image, ImageFilter, ImageStat



def analyze_quality(path):

    image = Image.open(
        path
    ).convert(
        "L"
    )


    # Оригинал и размытая версия

    blurred = image.filter(
        ImageFilter.GaussianBlur(
            radius=5
        )
    )


    pixels = list(
        image.getdata()
    )

    blur_pixels = list(
        blurred.getdata()
    )


    # Анализ резкости

    difference = []


    for original, blur in zip(
        pixels,
        blur_pixels
    ):

        difference.append(
            abs(
                original - blur
            )
        )


    sharpness = sum(
        difference
    ) / len(
        difference
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



    # Шум через края

    edges = image.filter(
        ImageFilter.FIND_EDGES
    )


    edge_stat = ImageStat.Stat(
        edges
    )


    noise_value = edge_stat.mean[0]


    if noise_value > 25:

        noise = "Высокий"

    elif noise_value > 10:

        noise = "Средний"

    else:

        noise = "Низкий"



    # Общая оценка

    score = (

        sharpness_score * 0.5

        +

        min(
            contrast * 2,
            100
        ) * 0.3

        +

        (100 - min(noise_value,100))
        * 0.2

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
            noise

    }
