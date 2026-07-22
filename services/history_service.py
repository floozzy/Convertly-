from database.history import (
    add_history,
    get_history,
    clear_history,
    total_operations
)


class HistoryService:

    @staticmethod
    def add(
        user_id,
        filename,
        operation
    ):

        add_history(
            user_id,
            filename,
            operation
        )

    @staticmethod
    def get(
        user_id,
        limit=20
    ):

        return get_history(
            user_id,
            limit
        )

    @staticmethod
    def clear(
        user_id
    ):

        clear_history(
            user_id
        )

    @staticmethod
    def total(
        user_id
    ):

        return total_operations(
            user_id
        )
