#https://qa-playground.com/ru/profile/backlog/manual?taskId=API-5

import allure
from config.docs import Documentation
from tests.basetest import BaseTest

class TestAddGames(BaseTest):

    @allure.title("Add game to wishlist")
    @allure.link(url=Documentation.ADD_ITEMS_WISHLIST, name="📕 Documentation")
    def test_add_game_wishlist(self):
        user_list = self.user_api.get_user_list()
        user_uuid = user_list.items[1].uuid
        games = self.games_api.get_all_games()
        game_uuid = games.items[0].uuid
        self.wishlists_api.add_item_to_users_wishlist(item_uuid=game_uuid, uuid=user_uuid)
        wishlist = self.wishlists_api.get_user_wishlist(user_uuid)
        print(wishlist)









