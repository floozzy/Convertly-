import hashlib


def calculate_hashes(path):

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()


    with open(
        path,
        "rb"
    ) as file:

        while True:

            chunk = file.read(
                8192
            )

            if not chunk:
                break


            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)


    return {

        "md5": md5.hexdigest(),

        "sha1": sha1.hexdigest(),

        "sha256": sha256.hexdigest()

    }
