#https://qa-playground.com/ru/profile/backlog/manual?taskId=API-4

import allure
from config.docs import Documentation
from tests.basetest import BaseTest

class TestUpdateUser(BaseTest):

    @allure.title("Update new user")
    @allure.link(url=Documentation.UPDATE_USERS, name="📕 Documentation")
    def test_update_user(self):
        user_list = self.user_api.get_user_list()
        user_uuid = user_list.items[0].uuid
        self.user_api.wrong_update_user(uuid=user_uuid)








