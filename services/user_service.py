from database.users import (
    create_user,
    get_user,
    add_file,
    add_stars,
    set_premium
)

from database.history import (
    total_operations
)

from database.purchases import (
    total_spent
)


class UserService:

    @staticmethod
    def register(user):

        create_user(user)

        return get_user(user.id)

    @staticmethod
    def profile(user_id):

        user = get_user(user_id)

        if user is None:
            return None

        return {
            "telegram_id": user[1],
            "username": user[2],
            "first_name": user[3],
            "premium": bool(user[4]),
            "stars": user[5],
            "files": user[6],
            "created": user[7],
            "operations": total_operations(user_id),
            "spent": total_spent(user_id)
        }

    @staticmethod
    def processed(user_id):

        add_file(user_id)

    @staticmethod
    def give_stars(user_id, stars):

        add_stars(user_id, stars)

    @staticmethod
    def activate_premium(user_id):

        set_premium(user_id, True)

    @staticmethod
    def deactivate_premium(user_id):

        set_premium(user_id, False)
