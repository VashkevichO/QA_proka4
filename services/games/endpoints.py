import os

STAGE = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "dev" else "https://release-gs.qa-playground.com/api/v1"

class Endpoints:

    game_list = f"{STAGE}/games"
    search_games = f"{STAGE}/games/search"


