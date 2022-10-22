import typing as t
import aiohttp

from .auth import AuthAPI
from .handlers import HandleResponse
from .exceptions import SilhouetteError

from utils import Config as config


class API(HandleResponse):
    API_PATH: t.Optional[str] = config.API_PATH
    NEXT_PATH: t.Optional[str] = None

    AUTH = AuthAPI()

    @property
    def get_base_path(self) -> t.Optional[str]:
        if self.NEXT_PATH is None:
            path = self.API_PATH
        else:
            path = self.API_PATH + self.NEXT_PATH
        return path

    async def _session_request_methods(
        self,
        path: str,
        method: str,
        *,
        data: dict = None
    ) -> t.Optional[t.Dict[str, t.Optional[str]]]:
        login = self.AUTH._get_login
        password = self.AUTH._get_password
        async with aiohttp.ClientSession(auth=aiohttp.BasicAuth(login, password)) as session:
            if data is None:
                try:
                    if method.lower() == "get":
                        request_method = await session.get(path)
                    if method.lower() == "delete":
                        request_method = await session.delete(path)
                except ValueError:
                    raise SilhouetteError
            else:
                try:
                    if method.lower() == "post":
                        request_method = await session.post(path, data=data)
                    if method.lower() == "put":
                        request_method = await session.put(path, data=data)
                except TypeError:
                    raise SilhouetteError
                except ValueError:
                    raise SilhouetteError
            async with request_method as response:
                return await self._handle_response(response)
