from PIL import Image, ImageDraw, ImageFont
import os



OUTPUT_DIR = "files/processed"



def get_font(size):

    fonts = [

        "/system/fonts/DroidSans.ttf",

        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",

        "DejaVuSans.ttf"

    ]


    for font in fonts:

        try:

            return ImageFont.truetype(
                font,
                size
            )

        except:

            pass


    return ImageFont.load_default()





def add_watermark(

    path,

    text="© Convertly",

    position="br",

    color=(255,255,255),

    opacity=200,

    font_size=80

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


        text_w = bbox[2]-bbox[0]

        text_h = bbox[3]-bbox[1]



        margin = 50



        positions = {


            "tl":

            (

                margin,

                margin

            ),



            "tc":

            (

                (image.width-text_w)//2,

                margin

            ),



            "tr":

            (

                image.width-text_w-margin,

                margin

            ),



            "c":

            (

                (image.width-text_w)//2,

                (image.height-text_h)//2

            ),



            "bl":

            (

                margin,

                image.height-text_h-margin

            ),



            "bc":

            (

                (image.width-text_w)//2,

                image.height-text_h-margin

            ),



            "br":

            (

                image.width-text_w-margin,

                image.height-text_h-margin

            )

        }



        xy = positions.get(

            position,

            positions["br"]

        )



        # тень под текст

        shadow = (

            xy[0]+3,

            xy[1]+3

        )


        draw.text(

            shadow,

            text,

            font=font,

            fill=(

                0,

                0,

                0,

                opacity

            )

        )



        # основной текст

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



        print(

            "✅ WATERMARK CREATED:",

            output

        )


        return output



    except Exception as e:


        print(

            "❌ WATERMARK ERROR:",

            e

        )


        return None
