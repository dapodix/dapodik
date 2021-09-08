from typing import List

from dapodik import DapodikResponse
from dapodik import DapodikResultData
from dapodik.base import BaseDapodik

from . import InfoSurveyPtm
from . import KerusakanBangunan
from . import PanelDashboard


class BaseBeranda(BaseDapodik):
    def getInfoSurveyPtm(self) -> InfoSurveyPtm:
        return self._get_struct("/getInfoSurveyPtm", InfoSurveyPtm)

    def getKerusakanBangunan(self) -> List[KerusakanBangunan]:
        result = self._get_struct(
            "/getKerusakanBangunan",
            DapodikResponse[List[KerusakanBangunan]],
        )
        assert result.rows is not None
        return result.rows

    def updatePanelDashboard(self) -> PanelDashboard:
        result = self._get_struct(
            "/updatePanelDashboard",
            DapodikResultData[PanelDashboard],
        )
        return result.data
