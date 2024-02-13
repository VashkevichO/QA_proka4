import allure
import requests
from typing import Union
from config.headers import Headers
from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from utils.helper import Helper
from services.users.models.model_user_list import UserListModel


class UsersAPI(Helper):

    def __init__(self):
        self.headers = Headers()
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    @allure.step("Get list all user")
    def get_user_list(self) -> UserListModel:
        response = requests.get(
            url=self.endpoints.list_all_users,
            headers=self.headers.basic,
            timeout=15
        )
        assert response.status_code == 200, response.json()
        model = UserListModel(**response.json())
        self.attach_response(response.json())
        return model

    @allure.step("Delete users")
    def delete_user(self, uuid):
        response = requests.delete(
            url=self.endpoints.delete_users(uuid),
            headers=self.headers.basic
        )
        assert response.status_code == 204, response.json()

    @allure.step("Check delete users")
    def check_delete_user(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user(uuid),
            headers=self.headers.basic,
            timeout=15
        )
        assert response.status_code == 404, response.json()

    def add_user(self):
        response_add_user = requests.post(
            url=self.endpoints.list_all_users,
            headers=self.headers.basic,
            json={
                "email": "130@ty.ru",
                "password": "string",
                "name": "Erfa0",
                "nickname": "Adkifra0"
            }
        )
        assert response_add_user.status_code == 200, response_add_user.json()


    def check_add_user(self):
        response = requests.get(
            url=self.endpoints.list_all_users,
            headers=self.headers.basic,
            timeout=15
        )
        assert response.status_code == 200, response.json()
        for key in response.json()["items"]:
            data = key
            print(data)
            assert isinstance(data, dict), "Response data is not a dictionary"
            assert "email" and "password" and "name" and "nickname" in data, "Expected 'title' and 'uuid' key not found in the JSON response"

    def wrong_update_user(self, uuid):
        response = requests.patch(
            url=self.endpoints.update_users(uuid),
            headers=self.headers.basic,
            json={
                "email": "123@ty.ru",
                "nickname": "Adkifra3",
            }
        )
        assert response.status_code == 409, response.json()
        assert "User email already exists:" in response.text, response.json()


