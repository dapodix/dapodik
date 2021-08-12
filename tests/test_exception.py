from dapodik.exception import DapodikException
from dapodik.exception import AuthException
from dapodik.exception import PasswordSalah
from dapodik.exception import PenggunaTidakTerdaftar
from dapodik.exception import PenggunaTidakDitemukan
from dapodik.exception import ServerTidakMerespon
from dapodik.exception import DapodikResponseError


def test_subclass():
    assert issubclass(DapodikException, BaseException)
    assert issubclass(AuthException, DapodikException)
    assert issubclass(PasswordSalah, AuthException)
    assert issubclass(PenggunaTidakTerdaftar, AuthException)
    assert issubclass(PenggunaTidakDitemukan, AuthException)
    assert issubclass(ServerTidakMerespon, DapodikException)
    assert issubclass(DapodikResponseError, DapodikException)
