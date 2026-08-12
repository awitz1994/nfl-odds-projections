from datetime import datetime, timezone

from app.services.cache import CacheService
from app.services.sportsbook import SportsbookService


class UpdateService:

    def __init__(
        self,
        sportsbook_service: SportsbookService,
        cache_service: CacheService,
    ):
        self.sportsbook = sportsbook_service
        self.cache = cache_service

    def refresh(self):
        try:
            odds = self.sportsbook.fetch_all()

        except Exception as exc:
            return {
                "success": False,
                "error": str(exc),
                "records": 0,
            }

        created_at = datetime.now(timezone.utc).isoformat()

        snapshot_id = self.cache.create_snapshot(
            created_at
        )

        self.cache.save_odds(
            snapshot_id,
            odds,
        )

        self.cache.mark_snapshot_successful(
            snapshot_id
        )

        return {
            "success": True,
            "error": None,
            "records": len(odds),
            "snapshot_id": snapshot_id,
        }