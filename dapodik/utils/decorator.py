from dapodik.base import DapodikObject


def set_meta(id: str):
    def deco(cls: DapodikObject):
        cls._id = id
        return cls

    return deco
