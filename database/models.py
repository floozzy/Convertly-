import sqlite3
from pathlib import Path

DB_PATH = Path("database/convertly.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():

    DB_PATH.parent.mkdir(exist_ok=True)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        username TEXT,
        first_name TEXT,
        premium INTEGER DEFAULT 0,
        stars INTEGER DEFAULT 0,
        files_processed INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        filename TEXT,
        operation TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS purchases(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        item TEXT,
        stars INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def add_user(user):

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


def get_user(telegram_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE telegram_id=?
        """,
        (telegram_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return row


def increase_counter(telegram_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET files_processed = files_processed + 1
        WHERE telegram_id=?
        """,
        (telegram_id,)
    )

    conn.commit()
    conn.close()


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
