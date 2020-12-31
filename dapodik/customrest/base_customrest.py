from dapodik import (
    BaseDapodik,
    Rest,
    MataPelajaranKurikulum,
    UpdatePanelDashboard,
)


class BaseCustomrest(BaseDapodik):
    def register_customrest(self) -> bool:
        try:
            self.MataPelajaranKurikulum = Rest(
                self, MataPelajaranKurikulum, "customrest/MataPelajaranKurikulum"
            )
            self.UpdatePanelDashboard = Rest(
                self, UpdatePanelDashboard, "customrest/UpdatePanelDashboard"
            )
            self.logger.debug("Berhasil memulai custom rest")
            return True
        except Exception as E:
            self.logger.exception(E)
            return False
