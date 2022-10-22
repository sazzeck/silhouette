import aiohttp
from json import JSONDecodeError

from .exceptions import SilhouetteError


class HandleResponse:
    async def _handle_response(self, response: aiohttp.ClientResponse) -> None:
        if response.status >= 400:
            raise SilhouetteError
        try:
            return await response.json()
        except JSONDecodeError:
            raise SilhouetteError
