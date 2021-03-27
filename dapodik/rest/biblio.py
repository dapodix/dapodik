import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class Biblio:
    id_biblio: str
    id_freq: Optional[str]
    id_publisher: str
    negara_id: str
    id_gmd: str
    id_classification: Optional[str]
    create_date: str
    title: str
    sor: Optional[str]
    edition: Optional[str]
    isbn_issn: Optional[str]
    collations: str
    publisher: Optional[str]
    publish_year: Optional[str]
    series_title: Optional[str]
    call_number: Optional[str]
    source: Optional[str]
    publish_place: Optional[str]
    notes: Optional[str]
    image: Optional[str]
    file_att: Optional[str]
    opac_hide: Optional[str]
    promoted: Optional[str]
    labels: Optional[str]
    paper_printing_spec: Optional[str]
    last_sync: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    id_publisher_str: str
    id_gmd_str: str
    tingkat_pendidikan_id: str
    tingkat_pendidikan_id_str: str

    def __str__(self):
        return self.title

    class Prop(BaseProp):
        @property
        def biblio(self) -> "Biblio":
            return self.dapodik._find(
                self.dapodik.biblio(),
                lambda x: x.id_biblio == getattr(self, "id_biblio"),
            )

        @biblio.setter
        def biblio(self, value: "Biblio"):
            new_id_biblio = self.dapodik._find(
                self.dapodik.biblio(),
                lambda x: x.id_biblio == value.id_biblio,
            )
            setattr(self, "id_biblio", new_id_biblio.id_biblio)
