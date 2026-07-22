import os


def analyze_file(path):

    size = os.path.getsize(path)

    extension = (
        os.path.splitext(path)[1]
        .replace(".", "")
        .lower()
    )


    return {
        "name": os.path.basename(path),
        "extension": extension,
        "size_mb": round(
            size / 1024 / 1024,
            2
        )
    }
