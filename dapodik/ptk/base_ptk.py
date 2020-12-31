from typing import List

from dapodik import (
    BaseDapodik,
    PtkTerdaftar,
    Ptk,
)


class BasePtk(BaseDapodik):
    def register_ptk(self) -> bool:
        try:
            self.Ptk = Ptk.maker(self, "rest/Ptk")
            self.PtkTerdaftar = PtkTerdaftar.maker(self, "rest/PtkTerdaftar")
            self.logger.debug("Berhasil memulai ptk")
            return True
        except Exception as E:
            self.logger.exception(E)
            return False

    @property
    def ptk(self) -> List[Ptk]:
        return self.Ptk()  # type: ignore

    @property
    def ptk_terdaftar(self) -> List[PtkTerdaftar]:
        return self.PtkTerdaftar()  # type: ignore
