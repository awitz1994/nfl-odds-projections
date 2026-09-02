from app.database import get_connection


class CacheService:

    def create_snapshot(self, created_at):
        with get_connection() as connection:

            cursor = connection.execute(
                """
                INSERT INTO snapshots (
                    created_at,
                    status
                )
                VALUES (?, ?)
                """,
                (created_at, "pending"),
            )

            return cursor.lastrowid

    def save_odds(self, snapshot_id, odds):
        with get_connection() as connection:

            connection.executemany(
                """
                INSERT INTO odds (
                    snapshot_id,
                    team,
                    sportsbook,
                    market,
                    line,
                    price,
                    updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        snapshot_id,
                        *odd,
                    )
                    for odd in odds
                ],
            )

    def mark_snapshot_successful(self, snapshot_id):
        with get_connection() as connection:

            connection.execute(
                """
                UPDATE snapshots
                SET status = ?
                WHERE id = ?
                """,
                ("successful", snapshot_id),
            )

    def get_all_odds(self):
        with get_connection() as connection:

            rows = connection.execute(
                """
                SELECT
                    odds.*
                FROM odds
                JOIN snapshots
                    ON odds.snapshot_id = snapshots.id
                WHERE snapshots.status = 'successful'
                AND snapshots.id = (
                    SELECT MAX(id)
                    FROM snapshots
                    WHERE status = 'successful'
                )
                ORDER BY
                    odds.team,
                    odds.sportsbook
                """
            ).fetchall()

            return [dict(row) for row in rows]

    def get_team_odds(self, team):
        with get_connection() as connection:

            rows = connection.execute(
                """
                SELECT
                    odds.*
                FROM odds
                JOIN snapshots
                    ON odds.snapshot_id = snapshots.id
                WHERE snapshots.status = 'successful'
                AND snapshots.id = (
                    SELECT MAX(id)
                    FROM snapshots
                    WHERE status = 'successful'
                )
                AND odds.team = ?
                ORDER BY odds.sportsbook
                """,
                (team,),
            ).fetchall()

            return [dict(row) for row in rows]