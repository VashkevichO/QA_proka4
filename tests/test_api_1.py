#https://qa-playground.com/ru/profile/backlog/manual?taskId=API-1

import allure
from config.docs import Documentation
from tests.basetest import BaseTest

class TestDeleteUser(BaseTest):

    @allure.title("Delete user")
    @allure.link(url=Documentation.DELETE_USER, name="📕 Documentation")
    def test_delete_user(self):

        users = self.user_api.get_user_list()
        user_uuid = users.items[2].uuid
        self.user_api.delete_user(uuid=user_uuid)
        self.user_api.check_delete_user(user_uuid)
        assert user_uuid not in users