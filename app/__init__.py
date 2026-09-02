import os
from flask import Flask

from app.api.routes import api_bp
from app.services.cache import CacheService
from app.services.sportsbook import SportsbookService
from app.services.update import UpdateService
from app.models.odds import create_tables


def create_app():
    app = Flask(__name__)

    # Initialize the database
    create_tables()

    # Create services
    cache_service = CacheService()
    sportsbook_service = SportsbookService(api_key=os.getenv("ODDS_API_KEY"))

    update_service = UpdateService(
        sportsbook_service=sportsbook_service,
        cache_service=cache_service
    )

    # # Register services
    app.cache_service = cache_service
    app.sportsbook_service = sportsbook_service
    app.update_service = update_service

    # Register blueprints
    app.register_blueprint(api_bp)

    return app