#https://qa-playground.com/ru/profile/backlog/manual?taskId=API-3

import allure
from config.docs import Documentation
from tests.basetest import BaseTest

class TestNewUser(BaseTest):

    @allure.title("Admin add new user")
    @allure.link(url=Documentation.SEARCH_GAMES, name="📕 Documentation")
    def test_new_user(self):
        user_list = self.user_api.get_user_list()
        self.user_api.add_user()
        self.user_api.check_add_user()



