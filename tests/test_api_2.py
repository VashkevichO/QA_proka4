#https://qa-playground.com/ru/profile/backlog/manual?taskId=API-1

import allure
from config.docs import Documentation
from tests.basetest import BaseTest

class TestSearchGames(BaseTest):

    @allure.title("Search Game")
    @allure.link(url=Documentation.SEARCH_GAMES, name="📕 Documentation")
    def test_search_games(self):
        games = self.games_api.get_all_games()
        self.games_api.search_games()
