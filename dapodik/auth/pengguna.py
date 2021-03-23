from bs4 import Tag
from typing import List

import attr


@attr.dataclass
class Pengguna:
    nama: str
    peran: str
    sekolah: str
    login_url: str
    photo: str

    @classmethod
    def from_li(cls, li: Tag, server: str = "") -> "Pengguna":
        a: Tag = li.find("a")
        spans: List[Tag] = li.findAll("span")
        login_url = str(server + a.attrs.get("href", "")[1:])
        # ERROR : bs4 parsing fault
        login_url = login_url.replace("¶ms", "&params")
        data = {
            "nama": spans[1].getText().split(":")[-1],
            "peran": spans[2].getText().split(":")[-1],
            "sekolah": spans[0].getText(),
            "login_url": login_url,
            "photo": server + a.find("img").attrs.get("src", ""),
        }
        return cls(**data)  # type: ignore

    @classmethod
    def from_soup(cls, soup: Tag, server: str = "") -> List["Pengguna"]:
        lis: List[Tag] = soup.findAll("li")
        results: List["Pengguna"] = list()
        for li in lis[1:-1]:
            results.append(cls.from_li(li, server))
        return results
