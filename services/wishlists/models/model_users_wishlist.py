from pydantic import BaseModel

class GameModel(BaseModel):
    title: str
    uuid: str

class UsersWishlistModel(BaseModel):
    items: list[GameModel]