import allure
from config.docs import Documentation
from tests.basetest import BaseTest


class TestUsers(BaseTest):

    @allure.title("Get list all users")
    @allure.link(url=Documentation.LIST_ALL_USERS, name="📕 Documentation")
    def test_get_all_users_list(self):
        users = self.user_api.get_user_list()
        user_uuid = users.items[6].uuid
        games = self.games_api.get_all_games()
        game_uuid = games.items[2].uuid
        game_name = games.items[2].title
        self.wishlists_api.add_item_to_users_wishlist(item_uuid=game_uuid, uuid=user_uuid)
        wishlist = self.wishlists_api.get_user_wishlist(user_uuid)

