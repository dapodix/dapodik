import logging
from dataclasses import asdict, dataclass
from requests import Session
from logging import Logger
from dapodik.dapodik import BASE_URL
from dapodik.rest import ChildDelete
from dapodik.utils import parse_rows_cast, parse_rows_update


class Base:
    _url: str = BASE_URL
    _logger: Logger = None


class BaseDapodik(Session, Base):

    def get_parse_cast_rows(self, url: str, Class_):
        outs = []
        try:
            res = self.get(self._url+url)
            if res.ok:
                datas: dict = res.json()
                outs = parse_rows_cast(datas, Class_)
        except Exception as e:
            self._logger.exception(e)
        finally:
            return outs


class Rest(Base):
    _id: str = None
    __url: str = None

    def __init__(self, session: Session, Class_, url: str, get=True, post=True, put=True, delete=True):
        self._session: Session = session
        self.__url: str = url
        self._get: bool = get
        self._post: bool = post
        self._put: bool = put
        self._delete: bool = delete
        self.__class = Class_
        self._logger = logging.getLogger(self.__class.__name__)

    def __call__(self):
        return self.get()

    def get(self):
        outs = []
        try:
            res = self._session.get(self._url+self.__url)
            if res.ok:
                datas: dict = res.json()
                self._id = datas.get('id')
                outs = parse_rows_cast(datas, self.__class, True)
        except Exception as e:
            self._logger.exception(e)
        finally:
            if len(outs) > 0:
                for obj in outs:
                    setattr(obj, '_session', self._session)
            return outs


class BaseData:
    _id: str = None
    _session: Session = None
    _url: str = BASE_URL
    __url: str = None

    @property
    def _data_id(self):
        return getattr(self, self._id)

    @property
    def _full_url(self):
        url = self._url
        url += self.__url if self.__url else ''
        url += f'/{self._data_id}' if self._id and self._data_id else ''
        return url

    def update(self, sync=True) -> bool:
        data = asdict(self)
        res = self._session.put(self._full_url, data=data)
        datas: dict = res.json()
        if not res.ok or not datas.get('success', False):
            return False
        if sync and 'rows' in datas:
            parse_rows_update(datas, self)
        return True

    def delete(self) -> bool:
        data = {
            self._id: self._data_id
        }
        params = {
            'sekolah_id': getattr(self, 'sekolah_id'),
        }
        res = self._session.delete(self._full_url, data=data, params=params)
        return res.ok and "'success' : true" in res.text

    def child_delete(self) -> [ChildDelete]:
        url = self._url
        url += 'rest/child_delete/'
        url += self._id
        params = {
            'id': self._data_id
        }
        res = self._session.get(url, params=params)
        return parse_rows_cast(res.json(), ChildDelete)
