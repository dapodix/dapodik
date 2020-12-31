from dapodik import BaseDapodik, Rest, Jadwal


class BaseJadwal(BaseDapodik):
    def register_jadwal(self) -> bool:
        try:
            self.Jadwal = Rest(self, Jadwal, "rest/Jadwal")
            self.logger.debug("Berhasil memulai jadwal")
            return True
        except Exception as E:
            self.logger.exception(E)
            return False
