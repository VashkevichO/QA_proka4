from services.users.api_users import UsersAPI
from services.wishlists.api_wishlists import WishlistsAPI
from services.games.api_games import GamesAPI


class BaseTest:


    def setup(self):
        self.user_api = UsersAPI()
        self.wishlists_api = WishlistsAPI()
        self.games_api = GamesAPI()