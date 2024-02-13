from pydantic import BaseModel

from pydantic import BaseModel

class GameModel(BaseModel):
    title: str
    uuid: str

class ListGamesModel(BaseModel):
    items: list[GameModel]