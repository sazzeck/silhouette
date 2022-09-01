import aiohttp

from json import JSONDecodeError


class SilhouetteError(Exception):
    pass


class SilhouetteAPI:
    API_PATH = "http://127.0.0.1:8080/api/silhouette/"
    NEXT_PATH = None

    def get_base_path(self):
        if self.NEXT_PATH is None:
            path = self.API_PATH
        if self.NEXT_PATH is not None:
            path = self.API_PATH + self.NEXT_PATH
        return path

    async def _handle_response(self, response):
        if response.status > 400:
            raise SilhouetteError
        try:
            return await response.json()
        except JSONDecodeError:
            raise SilhouetteError

    async def _session_request_methods(
        self,
        path: str,
        method: str,
        *,
        data: dict = None
    ):
        async with aiohttp.ClientSession() as session:
            if data is None:
                try:
                    if method.lower() == "get":
                        reuqest_method = await session.get(path)
                    if method.lower() == "delete":
                        reuqest_method = await session.delete(path)
                except ValueError:
                    raise SilhouetteError
            if data is not None:
                if isinstance(data, dict):
                    try:
                        if method.lower() == "post":
                            reuqest_method = await session.post(path, data=data)
                        if method.lower() == "put":
                            reuqest_method = await session.put(path, data=data)
                    except TypeError:
                        raise SilhouetteError
                    except ValueError:
                        raise SilhouetteError
            async with reuqest_method as response:
                return await self._handle_response(response)
