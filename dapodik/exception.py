class DapodikException(BaseException):
    pass


class AuthException(DapodikException):
    pass


class PasswordSalah(AuthException):
    pass


class PenggunaTidakTerdaftar(AuthException):
    pass


class ServerTidakMerespon(DapodikException):
    pass


class DapodikResponseError(DapodikException):
    pass
