from requests import Session
from logging import Logger
from dapodik.utils import parse_rows_cast


class BaseDapodik(Session):
    _url: str = "http://localhost:5774/"
    logger: Logger = None

    def get_parse_cast_rows(self, url: str, Class_):
        outs = []
        try:
            res = self.get(self._url+url)
            if res.ok:
                datas: dict = res.json()
                outs = parse_rows_cast(datas, Class_)
        except Exception as e:
            self.logger.exception(e)
        finally:
            return outs


class BaseRest:
    pass
