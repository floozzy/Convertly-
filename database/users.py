from database.models import get_connection


def create_user(user):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO users(
            telegram_id,
            username,
            first_name
        )
        VALUES(?,?,?)
        """,
        (
            user.id,
            user.username,
            user.first_name
        )
    )

    conn.commit()
    conn.close()


def get_user(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE telegram_id=?
        """,
        (user_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return row


def add_file(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET files_processed = files_processed + 1
        WHERE telegram_id=?
        """,
        (user_id,)
    )

    conn.commit()
    conn.close()


def add_stars(user_id, amount):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET stars = stars + ?
        WHERE telegram_id=?
        """,
        (amount, user_id)
    )

    conn.commit()
    conn.close()


def set_premium(user_id, value):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET premium=?
        WHERE telegram_id=?
        """,
        (
            1 if value else 0,
            user_id
        )
    )

    conn.commit()
    conn.close()
