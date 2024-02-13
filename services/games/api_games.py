import json
import allure
import requests
from typing import Union
from utils.helper import Helper
from config.headers import Headers
from services.games.endpoints import Endpoints
from services.games.payloads import Payloads
from services.games.models.model_games_model import ListGamesModel


class GamesAPI(Helper):

    def __init__(self):
        self.headers = Headers()
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    @allure.step("Get list all games")
    def get_all_games(self) -> ListGamesModel:
        response = requests.get(
            url=self.endpoints.game_list,
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        model = ListGamesModel(**response.json())
        self.attach_response(response.json())
        return model


    def search_games(self):
        response = requests.get(
            url=self.endpoints.search_games,
            headers=self.headers.basic,
            params={
                "query": "Atomic"
            }
        )

        assert response.status_code == 200, response.json()
        assert "Atomic" in response.text
        for key in response.json()["items"]:
            data = key
            print(data)
            assert isinstance(data, dict), "Response data is not a dictionary"
            assert "title" and "uuid" in data, "Expected 'title' and 'uuid' key not found in the JSON response"




