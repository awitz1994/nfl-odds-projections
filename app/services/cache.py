from app.database import get_connection


class CacheService:

    def save_odds(self, odds):

        with get_connection() as connection:

            cursor = connection.cursor()

            # Save odds here

            connection.commit()

    def get_all_odds(self):

        with get_connection() as connection:

            cursor = connection.cursor()

            cursor.execute("""
                SELECT *
                FROM odds
            """)

            rows = cursor.fetchall()

            return [dict(row) for row in rows]

    def get_team_odds(self, team):

        with get_connection() as connection:

            cursor = connection.cursor()

            cursor.execute("""
                SELECT *
                FROM odds
                WHERE team = ?
            """, (team,))

            rows = cursor.fetchall()

            return [dict(row) for row in rows]

    def clear(self):

        with get_connection() as connection:

            cursor = connection.cursor()

            cursor.execute("""
                DELETE FROM odds
            """)

            connection.commit()