import attr
from dapodik import DapodikObject


@attr.s(auto_attribs=True)
class UpdatePanelDashboard(DapodikObject):
    paneljumlahgtk: str
    paneljumlahguru: str
    paneljumlahtendik: str
    paneljumlahpns: str
    paneljumlahgty: str
    paneljumlahhonorer: str
    paneljumlahpd: str
    paneljumlahpdabk: str
    paneljumlahpdbantuanpd: str
    paneljumlahrombel: str
    paneljumlahrombelreguler: str
    paneljumlahrombeljauh: str
    paneljumlahrombelterbuka: str
    paneljumlahrk: str
    paneljumlahlab: str
    paneljumlahperpus: str
