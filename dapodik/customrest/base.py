from typing import List

from dapodik.base import BaseDapodik
from dapodik.utils.helper import cached

from . import Wilayah


class BaseCustomrest(BaseDapodik):
    @cached("kecamatan")
    def kecamatan(
        self, query: str, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Wilayah]:
        return self._get_rest(
            "kecamatan",
            List[Wilayah],
            page,
            start,
            limit,
            query=self._query(query=query),
            prefix="customrest/",
        )
