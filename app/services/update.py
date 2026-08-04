from app.services.cache import CacheService
from app.services.sportsbook import SportsbookService


class UpdateService:

    def __init__(
        self,
        sportsbook_service: SportsbookService,
        cache_service: CacheService
    ):
        self.sportsbook = sportsbook_service
        self.cache = cache_service

    def refresh(self):

        odds = self.sportsbook.fetch_all()

        self.cache.save_odds(odds)