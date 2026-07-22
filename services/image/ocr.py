import pytesseract

from PIL import Image



def extract_text(path):

    try:

        image = Image.open(
            path
        )


        text = pytesseract.image_to_string(
            image,
            lang="eng+rus"
        )


        text = text.strip()


        if not text:

            return None


        return text



    except Exception:

        return None
