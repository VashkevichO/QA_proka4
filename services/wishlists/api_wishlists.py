import allure
import requests
from typing import Union
from config.headers import Headers
from services.wishlists.endpoints import Endpoints
from services.wishlists.payloads import Payloads
from utils.helper import Helper
from services.wishlists.models.model_users_wishlist import UsersWishlistModel


class WishlistsAPI(Helper):

    def __init__(self):
        self.headers = Headers()
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    @allure.step("Add item to wishlist")
    def add_item_to_users_wishlist(self, item_uuid, uuid):
        response = requests.post(
            url=self.endpoints.add_item_to_wishlist(uuid),
            headers=self.headers.basic,
            json=self.payloads.add_item_payload(item_uuid)
        )
        assert response.status_code == 204, response.json()

    @allure.step("Get user wishlist")
    def get_user_wishlist(self, uuid):
        response = requests.get(
            url=self.endpoints.user_wishlist(uuid),
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        model = UsersWishlistModel(**response.json())
        self.attach_response(response.json())
        return model