user_files = {}


def save_file(user_id, path):
    user_files[user_id] = path


def get_file(user_id):
    return user_files.get(user_id)
