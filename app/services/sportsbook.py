import requests
from datetime import datetime, timezone


class SportsbookService:
    """
    Responsible for communicating with external sportsbooks.
    """
    BASE_URL = "https://api.odds-api.io/v3"
    SPORT = "american-football"

    NFL_LEAGUE = "usa-nfl"
    NFL_PRESEASON_LEAGUE = "usa-nfl-preseason"

    def __init__(self, api_key=None):
        self.api_key = api_key
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

    def get_nfl_events(self, include_preseason=False):
        league = (
            self.NFL_PRESEASON_LEAGUE
            if include_preseason
            else self.NFL_LEAGUE
        )

        response = requests.get(
            f"{self.BASE_URL}/events",
            params={
                "apiKey": self.api_key,
                "sport": self.SPORT,
                "league": league,
                "limit": 100,
            },
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    def get_event_odds(self, event_id, bookmakers):
        response = requests.get(
            f"{self.BASE_URL}/odds",
            params={
                "apiKey": self.api_key,
                "eventId": event_id,
                "bookmakers": ",".join(bookmakers),
            },
            timeout=10,
        )

        response.raise_for_status()

        return response.json()