import logging
import os
from datetime import datetime
from dapodik import Dapodik
from .backup_pd import BackupPd


class Backup(BackupPd):
    def __init__(self, dir: str, email: str, password: str, domain: str = None):
        self.dir: str = dir
        self.logger = logging.getLogger(self.__class__.__name__)
        self.dapodik: Dapodik = Dapodik(domain)
        if self.dapodik.login(email, password):
            self.logger.info('Berhasil masuk')
        else:
            raise ValueError('Gagal masuk ke dapodik')
