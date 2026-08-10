from app.database import get_connection


def create_tables():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS odds (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                team TEXT NOT NULL,
                sportsbook TEXT NOT NULL,
                market TEXT NOT NULL,
                line REAL,
                price INTEGER,
                updated_at TEXT
            )
            """
        )