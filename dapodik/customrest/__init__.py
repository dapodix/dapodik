from dapodik import BaseDapodik, Rest
from .mata_pelajaran_kurikulum import MataPelajaranKurikulum
from .update_panel_dashboard import UpdatePanelDashboard


class BaseCustomRest(BaseDapodik):
    def register_custom_rest(self) -> bool:
        try:
            self.MataPelajaranKurikulum = Rest(
                self, MataPelajaranKurikulum,
                'customrest/MataPelajaranKurikulum')
            self.UpdatePanelDashboard = Rest(
                self, UpdatePanelDashboard,
                'customrest/UpdatePanelDashboard')
            self.logger.debug('Berhasil memulai custom rest')
            return True
        except Exception as E:
            self.logger.exception(E)
            return False
