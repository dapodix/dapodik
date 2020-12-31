from typing import List

from dapodik import (
    BaseDapodik,
    Tanah,
    Bangunan,
    Ruang,
    Alat,
    Angkutan,
    Buku,
    TanahLongitudinal,
    TanahDariBlockgrant,
    BangunanLongitudinal,
    BangunanDariBlockgrant,
    RuangLongitudinal,
    AlatLongitudinal,
    AlatDariBlockgrant,
    AngkutanDariBlockgrant,
    BukuLongitudinal,
)


class BaseSarpras(BaseDapodik):
    def register_sarpras(self):
        try:
            self.Alat = Alat.maker(self, "rest/Alat")
            self.AlatDariBlockgrant = AlatDariBlockgrant.maker(
                self, "rest/AlatDariBlockgrant"
            )
            self.AlatLongitudinal = AlatLongitudinal.maker(
                self, "rest/AlatLongitudinal"
            )
            self.Bangunan = Bangunan.maker(self, "rest/Bangunan")
            self.BangunanDariBlockgrant = BangunanDariBlockgrant.maker(
                self, "rest/BangunanDariBlockgrant"
            )
            self.BangunanLongitudinal = BangunanLongitudinal.maker(
                self, "rest/BangunanLongitudinal"
            )
            self.Ruang = Ruang.maker(self, "rest/Ruang")
            self.RuangLongitudinal = RuangLongitudinal.maker(
                self, "rest/RuangLongitudinal"
            )
            self.Tanah = Tanah.maker(self, "rest/Tanah")
            self.TanahLongitudinal = TanahLongitudinal.maker(
                self, "rest/TanahLongitudinal"
            )
            self.TanahDariBlockgrant = TanahDariBlockgrant.maker(
                self, "rest/TanahDariBlockgrant"
            )
            self.Angkutan = Angkutan.maker(self, "rest/Angkutan")
            self.Buku = Buku.maker(self, "rest/Buku")
            self.AngkutanDariBlockgrant = AngkutanDariBlockgrant.maker(
                self, "rest/AngkutanDariBlockgrant"
            )
            self.BukuLongitudinal = BukuLongitudinal.maker(
                self, "rest/BukuLongitudinal"
            )
            self.logger.debug("Berhasil memulai sarpras")
            return True
        except Exception as E:
            self.logger.exception(E)
            return False

    @property
    def alat(self) -> List[Alat]:
        return self.Alat()  # type: ignore

    @property
    def alat_dari_blockgrant(self) -> List[AlatDariBlockgrant]:
        return self.AlatDariBlockgrant()  # type: ignore

    @property
    def alat_longitudinal(self) -> List[AlatLongitudinal]:
        return self.AlatLongitudinal()  # type: ignore

    @property
    def bangunan(self) -> List[Bangunan]:
        return self.Bangunan()  # type: ignore

    @property
    def bangunan_dari_blockgrant(self) -> List[BangunanDariBlockgrant]:
        return self.BangunanDariBlockgrant()  # type: ignore

    @property
    def bangunan_longitudinal(self) -> List[BangunanLongitudinal]:
        return self.BangunanLongitudinal()  # type: ignore

    @property
    def ruang(self) -> List[Ruang]:
        return self.Ruang()  # type: ignore

    @property
    def ruang_longitudinal(self) -> List[RuangLongitudinal]:
        return self.RuangLongitudinal()  # type: ignore

    @property
    def tanah(self) -> List[Tanah]:
        return self.Tanah()  # type: ignore

    @property
    def tanah_longitudinal(self) -> List[TanahLongitudinal]:
        return self.TanahLongitudinal()  # type: ignore

    @property
    def tanah_dari_blockgrant(self) -> List[TanahDariBlockgrant]:
        return self.TanahDariBlockgrant()  # type: ignore

    @property
    def angkutan(self) -> List[Angkutan]:
        return self.Angkutan()  # type: ignore

    @property
    def buku(self) -> List[Buku]:
        return self.Buku()  # type: ignore

    @property
    def angkutan_dari_blockgrant(self) -> List[AngkutanDariBlockgrant]:
        return self.AngkutanDariBlockgrant()  # type: ignore

    @property
    def buku_longitudinal(self) -> List[BukuLongitudinal]:
        return self.BukuLongitudinal()  # type: ignore
