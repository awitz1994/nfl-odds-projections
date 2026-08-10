from app.database import get_connection


def create_tables():
    with get_connection() as connection:

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS snapshots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                status TEXT NOT NULL
            )
            """
        )

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS odds (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                snapshot_id INTEGER NOT NULL,
                team TEXT NOT NULL,
                sportsbook TEXT NOT NULL,
                market TEXT NOT NULL,
                line REAL,
                price INTEGER,
                updated_at TEXT NOT NULL,
                FOREIGN KEY (snapshot_id)
                    REFERENCES snapshots (id)
            )
            """
        )