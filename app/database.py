import sqlite3

from app.config import DATABASE


def get_connection():
    connection = sqlite3.connect(
        DATABASE,
        check_same_thread=False
    )
    connection.row_factory = sqlite3.Row
    return connection