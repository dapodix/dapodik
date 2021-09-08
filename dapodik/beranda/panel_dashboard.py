import attr


@attr.dataclass
class PanelDashboard:
    paneljumlahgtk: int
    paneljumlahguru: int
    paneljumlahtendik: int
    paneljumlahpns: int
    paneljumlahgty: int
    paneljumlahhonorer: int
    paneljumlahpd: int
    paneljumlahpdabk: int
    paneljumlahpdbantuanpd: int
    paneljumlahrombel: int
    paneljumlahrombelreguler: int
    paneljumlahrombeljauh: int
    paneljumlahrombelterbuka: int
    paneljumlahrk: int
    paneljumlahlab: int
    paneljumlahperpus: int

    @property
    def gtk(self) -> int:
        return self.paneljumlahgtk

    @property
    def guru(self) -> int:
        return self.paneljumlahguru

    @property
    def tendik(self) -> int:
        return self.paneljumlahtendik

    @property
    def pns(self) -> int:
        return self.paneljumlahpns

    @property
    def gty(self) -> int:
        return self.paneljumlahgty

    @property
    def honorer(self) -> int:
        return self.paneljumlahhonorer

    @property
    def pd(self) -> int:
        return self.paneljumlahpd

    @property
    def pdabk(self) -> int:
        return self.paneljumlahpdabk

    @property
    def pdbantuanpd(self) -> int:
        return self.paneljumlahpdbantuanpd

    @property
    def rombel(self) -> int:
        return self.paneljumlahrombel

    @property
    def rombelreguler(self) -> int:
        return self.paneljumlahrombelreguler

    @property
    def rombeljauh(self) -> int:
        return self.paneljumlahrombeljauh

    @property
    def rombelterbuka(self) -> int:
        return self.paneljumlahrombelterbuka

    @property
    def rk(self) -> int:
        return self.paneljumlahrk

    @property
    def lab(self) -> int:
        return self.paneljumlahlab

    @property
    def perpus(self) -> int:
        return self.paneljumlahperpus
