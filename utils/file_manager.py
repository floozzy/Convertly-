import os
import time


MAX_SIZE = 50 * 1024 * 1024



def check_size(path):

    size = os.path.getsize(path)

    return size <= MAX_SIZE



def cleanup(folder="files"):

    now = time.time()


    for file in os.listdir(folder):

        path = os.path.join(
            folder,
            file
        )

        if os.path.isfile(path):

            if now - os.path.getmtime(path) > 3600:

                os.remove(path)
