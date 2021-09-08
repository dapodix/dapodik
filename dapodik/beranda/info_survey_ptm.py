import attr


@attr.dataclass
class InfoSurveyPtm:
    success: bool
    is_ngisi: bool
    message: str

    def __bool__(self):
        return self.is_ngisi

    def __str__(self):
        return self.message
