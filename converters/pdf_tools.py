from PIL import Image
from pypdf import PdfWriter, PdfReader


def images_to_pdf(files):

    imgs=[]

    for file in files:
        img = Image.open(file).convert("RGB")
        imgs.append(img)


    output="convertly_pdf.pdf"

    imgs[0].save(
        output,
        save_all=True,
        append_images=imgs[1:]
    )

    return output



def merge_pdf(files):

    writer = PdfWriter()


    for file in files:

        reader = PdfReader(file)

        for page in reader.pages:
            writer.add_page(page)


    output="merged.pdf"


    with open(output,"wb") as f:
        writer.write(f)


    return output
