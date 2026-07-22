from database.models import get_connection


def add_history(
    telegram_id,
    filename,
    operation
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history(
            telegram_id,
            filename,
            operation
        )
        VALUES(?,?,?)
        """,
        (
            telegram_id,
            filename,
            operation
        )
    )

    conn.commit()
    conn.close()


def get_history(
    telegram_id,
    limit=20
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            filename,
            operation,
            created_at
        FROM history
        WHERE telegram_id=?
        ORDER BY id DESC
        LIMIT ?
        """,
        (
            telegram_id,
            limit
        )
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def clear_history(
    telegram_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM history
        WHERE telegram_id=?
        """,
        (telegram_id,)
    )

    conn.commit()
    conn.close()


def total_operations(
    telegram_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM history
        WHERE telegram_id=?
        """,
        (telegram_id,)
    )

    total = cursor.fetchone()[0]

    conn.close
