import os

STAGE = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "dev" else "https://release-gs.qa-playground.com/api/v1"

class Endpoints:

    add_item_to_wishlist = lambda self, uuid: f"{STAGE}/users/{uuid}/wishlist/add"
    user_wishlist = lambda self, uuid: f"{STAGE}/users/{uuid}/wishlist"