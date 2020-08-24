from dapodik import (
    BaseDapodik,
    Rest,
    Tanah,
    Bangunan,
    Ruang,
    Alat,
    Angkutan,
    Buku,
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
            self.Alat = Rest(self, Alat, 'rest/Alat')
            self.AlatDariBlockgrant = Rest(self, AlatDariBlockgrant,
                                           'rest/AlatDariBlockgrant')
            self.AlatLongitudinal = Rest(self, AlatLongitudinal,
                                         'rest/AlatLongitudinal')
            self.Bangunan = Rest(self, Bangunan, 'rest/Bangunan')
            self.BangunanDariBlockgrant = Rest(self, BangunanDariBlockgrant,
                                               'rest/BangunanDariBlockgrant')
            self.BangunanLongitudinal = Rest(self, BangunanLongitudinal,
                                             'rest/BangunanLongitudinal')
            self.Ruang = Rest(self, Ruang, 'rest/Ruang')
            self.RuangLongitudinal = Rest(self, RuangLongitudinal,
                                          'rest/RuangLongitudinal')
            self.Tanah = Rest(self, Tanah, 'rest/Tanah')
            self.Angkutan = Rest(self, Angkutan, 'rest/Angkutan')
            self.Buku = Rest(self, Buku, 'rest/Buku')
            self.AngkutanDariBlockgrant = Rest(self, AngkutanDariBlockgrant,
                                               'rest/AngkutanDariBlockgrant')
            self.BukuLongitudinal = Rest(self, BukuLongitudinal,
                                         'rest/BukuLongitudinal')
            self.logger.debug('Berhasil memulai sarpras')
            return True
        except Exception as E:
            self.logger.exception(E)
            return False
