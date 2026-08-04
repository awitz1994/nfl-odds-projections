import requests


class SportsbookService:
    """
    Responsible for communicating with external sportsbooks.
    """

    def __init__(self):
        self.session = requests.Session()

    def fetch_all(self):
        """Fetch odds from all configured sportsbooks."""
        pass

    def fetch_draftkings(self):
        pass

    def fetch_fanduel(self):
        pass