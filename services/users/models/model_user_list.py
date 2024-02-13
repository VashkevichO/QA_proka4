from pydantic import BaseModel

class Item(BaseModel):
    email: str
    name: str
    nickname: str
    uuid: str

class Meta(BaseModel):
    total: int

class UserListModel(BaseModel):
    items: list[Item]
    meta: Meta
