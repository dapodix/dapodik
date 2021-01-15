class AuthException(BaseException):
    pass


class PasswordSalah(AuthException):
    pass


class PenggunaTidakTerdaftar(AuthException):
    pass
