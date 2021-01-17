class Defaults:
    def __init__(
        self,
        sekolah_id: str = "",
        page: int = 1,
        start: int = 0,
        limit: int = 25,
        **kwargs,
    ):
        self.sekolah_id = sekolah_id
        self.page = page
        self.start = start
        self.limit = limit
        for k, v in kwargs.items():
            setattr(self, k, v)
