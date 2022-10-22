from datetime import datetime
import typing as t

from django.contrib.auth.hashers import make_password

from . import API, SilhouetteError


class SilhouetteUser(API):
    NEXT_PATH = "user/"

    async def is_exists(
        self,
        user_id: t.Optional[int]
    ) -> bool:
        try:
            await self.fetch_user(user_id)
            return True
        except SilhouetteError:
            return False

    def _create_password(
        self,
        password: t.Optional[str]
    ) -> t.Optional[str]:
        if password is not None:
            pwd = make_password(password)
            return pwd

    async def create_user(
        self,
        user_id: t.Optional[int],
        username: t.Optional[str],
        password: t.Optional[str],
    ) -> None:
        path = self.get_base_path
        user = {
            "id": user_id,
            "username": username,
            "password": self._create_password(password),
        }

        await self._session_request_methods(path, "post", data=user)

    async def fetch_all_users(self) -> t.List[dict]:
        path = self.get_base_path
        return await self._session_request_methods(path, "get")

    async def fetch_user(self, user_id: t.Optional[int]) -> t.Dict[str, t.Optional[str]]:
        path = self.get_base_path + f"{user_id}/"
        return await self._session_request_methods(path, "get")

    async def fetch_date_registration(self, user_id: t.Optional[int]) -> t.Optional[datetime]:
        user = await self.fetch_user(user_id)
        return user.get("date_joined")

    async def fetch_last_login(self, user_id: t.Optional[int]) -> t.Optional[datetime]:
        user = await self.fetch_user(user_id)
        return user.get("last_login")
