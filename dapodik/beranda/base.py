import cattr
import json

from dapodik import DapodikResultData
from dapodik.base import BaseDapodik

from . import PanelDashboard


class BaseBeranda(BaseDapodik):
    def updatePanelDashboard(self) -> PanelDashboard:
        res = self._get("/updatePanelDashboard")
        data = json.loads(res.text)
        result = cattr.structure(data, DapodikResultData[PanelDashboard])
        return result.data
