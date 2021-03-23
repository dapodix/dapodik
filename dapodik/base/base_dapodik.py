import logging
from requests import Response, Session
from typing import Any


class BaseDapodik(object):
    def __init__(self, base_url: str = "http://localhost:5774/"):
        self._logger = logging.getLogger("Dapodik")
        self._session = Session()
        self._base_url = base_url

    @property
    def logger(self) -> logging.Logger:
        return self._logger

    @property
    def session(self) -> Session:
        return self._session

    @property
    def base_url(self) -> str:
        return self._base_url

    def _url(self, path: str) -> str:
        if path.startswith(self.base_url):
            return path
        return self.base_url + path.lstrip("/")

    def _rest_url(self, name: str) -> str:
        return self._url("rest/" + name.lstrip("/"))

    def _post(
        self,
        url: str,
        data: dict = None,
        json: dict = None,
        params: dict = None,
        headers: dict = None,
        **kwargs: Any,
    ) -> Response:
        return self.session.post(
            self._url(url),
            data=data,
            json=json,
            params=params,
            headers=headers,
            **kwargs,
        )

    def _get(
        self,
        url: str,
        params: dict = None,
        **kwargs: Any,
    ) -> Response:
        return self.session.get(
            self._url(url),
            params=params,
            **kwargs,
        )
