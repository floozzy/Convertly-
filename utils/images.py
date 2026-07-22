last_images = {}



def save_image(
    user_id,
    path
):

    last_images[user_id] = path


    print(
        "IMAGE MEMORY:",
        user_id,
        path
    )





def get_image(
    user_id
):

    return last_images.get(
        user_id
    )
