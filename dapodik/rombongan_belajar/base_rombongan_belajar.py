from typing import List

from dapodik import (
    BaseDapodik,
    Pembelajaran,
    RombonganBelajar,
)


class BaseRombonganBelajar(BaseDapodik):
    def register_rombongan_belajar(self) -> bool:
        try:
            self.Pembelajaran = Pembelajaran.maker(self, "rest/Pembelajaran")
            self.RombonganBelajar = RombonganBelajar.maker(
                self, "rest/RombonganBelajar"
            )
            self.logger.debug("Berhasil memulai rombongan belajar")
            return True
        except Exception as E:
            self.logger.exception(E)
            return False

    def pembelajaran(self) -> List[Pembelajaran]:
        return self.Pembelajaran()  # type: ignore

    def rombonganbelajar(self) -> List[RombonganBelajar]:
        return self.RombonganBelajar()  # type: ignore
