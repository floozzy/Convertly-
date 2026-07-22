from PIL import Image, ImageDraw, ImageFont
import os



OUTPUT_DIR = "files/processed"



POSITIONS = {


    "top_left":

        "top_left",


    "top_center":

        "top_center",


    "top_right":

        "top_right",


    "center":

        "center",


    "bottom_left":

        "bottom_left",


    "bottom_center":

        "bottom_center",


    "bottom_right":

        "bottom_right"

}




def get_font(size):

    try:

        return ImageFont.truetype(

            "DejaVuSans.ttf",

            size

        )

    except:

        return ImageFont.load_default()





def calculate_position(
    image_size,
    text_size,
    position,
    margin
):


    width, height = image_size


    text_width, text_height = text_size



    positions = {


        "top_left":

            (

                margin,

                margin

            ),



        "top_center":

            (

                (width-text_width)//2,

                margin

            ),



        "top_right":

            (

                width-text_width-margin,

                margin

            ),



        "center":

            (

                (width-text_width)//2,

                (height-text_height)//2

            ),



        "bottom_left":

            (

                margin,

                height-text_height-margin

            ),



        "bottom_center":

            (

                (width-text_width)//2,

                height-text_height-margin

            ),



        "bottom_right":

            (

                width-text_width-margin,

                height-text_height-margin

            )

    }



    return positions.get(

        position,

        positions["bottom_right"]

    )





def add_watermark(

    path,

    text="© Convertly",

    position="bottom_right",

    color=(255,255,255),

    opacity=120,

    font_size=50,

    margin=40

):


    try:


        os.makedirs(

            OUTPUT_DIR,

            exist_ok=True

        )



        image = Image.open(

            path

        ).convert(

            "RGBA"

        )



        watermark = Image.new(

            "RGBA",

            image.size,

            (0,0,0,0)

        )



        draw = ImageDraw.Draw(

            watermark

        )



        font = get_font(

            font_size

        )



        bbox = draw.textbbox(

            (0,0),

            text,

            font=font

        )



        text_width = bbox[2]-bbox[0]

        text_height = bbox[3]-bbox[1]



        xy = calculate_position(

            image.size,

            (

                text_width,

                text_height

            ),

            position,

            margin

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

            watermark

        )



        filename = (

            "watermarked_"

            +

            os.path.basename(path)

        )



        output = os.path.join(

            OUTPUT_DIR,

            filename

        )



        result.convert(

            "RGB"

        ).save(

            output,

            quality=95

        )



        return output



    except Exception as e:


        print(

            "Watermark error:",

            e

        )


        return None
