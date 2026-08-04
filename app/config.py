import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join(BASE_DIR, "odds.db")

ODDS_API_KEY = os.getenv("ODDS_API_KEY")