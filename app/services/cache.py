from app.database import get_connection


class CacheService:

    def save_odds(self, odds):
        with get_connection() as connection:
            connection.executemany(
                """
                INSERT INTO odds (
                    team,
                    sportsbook,
                    market,
                    line,
                    price,
                    updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                odds
            )

    def get_all_odds(self):
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT *
                FROM odds
                ORDER BY team, sportsbook
                """
            ).fetchall()

            return [dict(row) for row in rows]

    def get_team_odds(self, team):
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT *
                FROM odds
                WHERE team = ?
                ORDER BY sportsbook
                """,
                (team,)
            ).fetchall()

            return [dict(row) for row in rows]

    def clear(self):
        with get_connection() as connection:
            connection.execute("DELETE FROM odds")