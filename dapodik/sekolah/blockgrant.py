from dataclasses import dataclass
from typing import Union


@dataclass
class BlockGrant:
    blockgrant_id: str
    sekolah_id: str
    nama: str
    tahun: str
    jenis_bantuan_id: 5
    sumber_dana_id: str
    besar_bantuan: str
    dana_pendamping: str
    peruntukan_dana: Union[str, None]
    asal_data: str
    create_date: str
    last_update: str
    soft_delete: str
    last_sync: str
    updater_id: str
    sekolah_id_str: str
    jenis_bantuan_id_str: str
    sumber_dana_id_str: str
