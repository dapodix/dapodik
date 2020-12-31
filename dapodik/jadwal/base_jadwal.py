from typing import List

from dapodik import BaseDapodik, Jadwal


class BaseJadwal(BaseDapodik):
    def register_jadwal(self) -> bool:
        try:
            self.Jadwal = Jadwal.maker(self, "rest/Jadwal")
            self.logger.debug("Berhasil memulai jadwal")
            return True
        except Exception as E:
            self.logger.exception(E)
            return False

    @property
    def jadwal(self) -> List[Jadwal]:
        return self.Jadwal()  # type: ignore
