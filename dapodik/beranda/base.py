import cattr
import json

from dapodik import DapodikResultData
from dapodik.base import BaseDapodik

from . import InfoSurveyPtm
from . import PanelDashboard


class BaseBeranda(BaseDapodik):
    def getInfoSurveyPtm(self) -> InfoSurveyPtm:
        res = self._get("/getInfoSurveyPtm")
        data = json.loads(res.text)
        return cattr.structure(data, InfoSurveyPtm)

    def updatePanelDashboard(self) -> PanelDashboard:
        res = self._get("/updatePanelDashboard")
        data = json.loads(res.text)
        result = cattr.structure(data, DapodikResultData[PanelDashboard])
        return result.data
