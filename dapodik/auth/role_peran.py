from __future__ import annotations
import attr
from bs4 import Tag
from typing import Optional, List
from dapodik.config import DOMAIN


@attr.dataclass
class Roleperan:
    nama: Optional[str]
    peran: Optional[str]
    lembaga: Optional[str]
    url: str

    @classmethod
    def from_tag(cls, tag: Tag) -> Roleperan:
        a: Tag = tag.find("a")
        spans: List[Tag] = a.find_all("span")
        url = DOMAIN + str(a["href"])
        data = {
            "nama": str(spans[1].text).split(":")[-1],
            "peran": str(spans[2].text).split(":")[-1],
            "lembaga": str(spans[0].text).split(":")[-1],
            "url": url,
        }
        return cls(**data)

    def __str__(self):
        strs = [self.nama, self.peran, self.lembaga]
        return " - ".join(strs)
