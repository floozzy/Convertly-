from database.models import get_connection


def add_purchase(
    telegram_id,
    item,
    stars
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO purchases(
            telegram_id,
            item,
            stars
        )
        VALUES(?,?,?)
        """,
        (
            telegram_id,
            item,
            stars
        )
    )

    conn.commit()
    conn.close()


def get_purchases(
    telegram_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            item,
            stars,
            created_at
        FROM purchases
        WHERE telegram_id=?
        ORDER BY id DESC
        """,
        (telegram_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def total_spent(
    telegram_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COALESCE(SUM(stars), 0)
        FROM purchases
        WHERE telegram_id=?
        """,
        (telegram_id,)
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def has_premium(
    telegram_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT premium
        FROM users
        WHERE telegram_id=?
        """,
        (telegram_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return False

    return bool(row[0])
