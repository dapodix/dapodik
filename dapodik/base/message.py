from . import dataclass


@dataclass
class Message:
    success: bool = True
    message: str

    def __str__(self):
        return self.message

    def __bool__(self):
        return self.success
