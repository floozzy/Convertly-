from PIL import Image, ImageDraw, ImageFont
import os



OUTPUT_DIR = "files/processed"



def get_font(size):

    try:

        return ImageFont.truetype(
            "DejaVuSans.ttf",
            size
        )

    except:

        return ImageFont.load_default()



def add_watermark(

    path,

    text,

    position,

    color,

    opacity,

    font_size

):


    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )


    image = Image.open(
        path
    ).convert(
        "RGBA"
    )


    layer = Image.new(
        "RGBA",
        image.size,
        (0,0,0,0)
    )


    draw = ImageDraw.Draw(
        layer
    )


    font = get_font(
        font_size
    )


    bbox = draw.textbbox(
        (0,0),
        text,
        font=font
    )


    w = bbox[2]-bbox[0]

    h = bbox[3]-bbox[1]



    margin = 40


    positions = {


        "tl":
        (
            margin,
            margin
        ),


        "tc":
        (
            (image.width-w)//2,
            margin
        ),


        "tr":
        (
            image.width-w-margin,
            margin
        ),


        "c":
        (
            (image.width-w)//2,
            (image.height-h)//2
        ),


        "bl":
        (
            margin,
            image.height-h-margin
        ),


        "bc":
        (
            (image.width-w)//2,
            image.height-h-margin
        ),


        "br":
        (
            image.width-w-margin,
            image.height-h-margin
        )

    }



    xy = positions.get(
        position,
        positions["br"]
    )



    draw.text(
        xy,
        text,
        font=font,
        fill=(
            color[0],
            color[1],
            color[2],
            opacity
        )
    )



    result = Image.alpha_composite(
        image,
        layer
    )



    output = os.path.join(

        OUTPUT_DIR,

        "watermark_"
        +
        os.path.basename(path)

    )



    result.convert(
        "RGB"
    ).save(
        output,
        quality=95
    )


    return output
