import typing as t

from .handlers import HandleResponse

from .exceptions import SilhouetteAuthError

from utils import Config as config


class AuthAPI(HandleResponse):
    __API_AUTH_PATH: t.Optional[str] = config.API_AUTH_PATH
    __LOGIN: t.Optional[str] = config.API_LOGIN
    __PASSWORD: t.Optional[str] = config.API_PASSWORD

    @property
    def _get_auth_path(self) -> t.Optional[str]:
        return self.__API_AUTH_PATH

    @property
    def _get_login(self) -> t.Optional[str]:
        if self.__LOGIN:
            return self.__LOGIN
        raise SilhouetteAuthError

    @property
    def _get_password(self) -> t.Optional[str]:
        if self.__PASSWORD:
            return self.__PASSWORD
        raise SilhouetteAuthError
