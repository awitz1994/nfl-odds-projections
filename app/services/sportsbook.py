import requests
from datetime import datetime, timezone


class SportsbookService:
    """
    Responsible for communicating with external sportsbooks.
    """

    def __init__(self, api_key=None):
        self.api_key = api_key
        print(f"API key configured: {bool(self.api_key)}")
        self.session = requests.Session()

    def fetch_all(self):
        """Fetch odds from all configured sportsbooks."""
        now = datetime.now(timezone.utc).isoformat()

        return [
            (
                "Kansas City Chiefs",
                "DraftKings",
                "wins",
                11.5,
                -110,
                now,
            ),
            (
                "Kansas City Chiefs",
                "FanDuel",
                "wins",
                11.0,
                -105,
                now,
            ),
            (
                "Buffalo Bills",
                "DraftKings",
                "wins",
                10.5,
                -115,
                now,
            ),
            (
                "Buffalo Bills",
                "FanDuel",
                "wins",
                11.0,
                -110,
                now,
            ),
        ]

    def fetch_draftkings(self):
        pass

    def fetch_fanduel(self):
        pass