from logging import Logger
from dapodik import Dapodik


class BaseBackup:
    dapodik: Dapodik = None
    logger: Logger = None
    dir: str = None
