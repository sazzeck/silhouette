from . import SilhouetteAPI


class UsersAPI(SilhouetteAPI):
    NEXT_PATH = "user/"

    async def fetch_all_users(self):
        path = self.get_base_path()
        return await self._session_request_methods(path, "get")

    async def fetch_user(self, user_id: int = None):
        path = self.get_base_path() + f"{user_id}/"
        return await self._session_request_methods(path, "get")

    async def create_user(
        self,
        user_id: int = None,
        username: str = None,
        firstname: str = None,
        lastname: str = None
    ):
        path = self.get_base_path()
        user = {}
        if user_id is not None:
            user["id"] = user_id
        if username is not None:
            user["username"] = username
        if firstname is not None:
            user["first_name"] = firstname
        if lastname is not None:
            user["last_name"] = lastname
        await self._session_request_methods(path, "post", data=user)

    async def create_password(self):
        pass

    async def update_password(self):
        pass
