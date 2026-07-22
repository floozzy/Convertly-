from PIL import Image
from fpdf import FPDF



def images_to_pdf(images, output):

    pdf = FPDF()


    for img in images:

        image = Image.open(img)

        width, height = image.size


        pdf.add_page()

        pdf.image(
            img,
            x=10,
            y=10,
            w=190
        )


    pdf.output(output)


    return output
