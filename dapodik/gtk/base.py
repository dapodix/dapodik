from functools import partialmethod
from typing import List, Optional

from dapodik.base import BaseDapodik
from dapodik.version import __tahun_ajaran__

from . import PtkTerdaftar
from . import Ptk


class BaseGtk(BaseDapodik):
    def ptk(
        self,
        sekolah_id: str,
        tahun_ajaran_id: str = __tahun_ajaran__,
        ptk_module: Optional[str] = None,
        jenis_gtk: Optional[str] = None,
        limit: int = 25,
        penugasan_null: Optional[int] = None,
        page: int = 1,
        start: int = 0,
    ) -> List[Ptk]:
        """ptk mengambil data ptk

        Args:
            sekolah_id (str): Sekolah ID
            tahun_ajaran_id (str, optional): Id tahun ajaran. Defaults to __tahun_ajaran__.
            ptk_module (Optional[str], optional): antara `ptkterdaftar` dan `ptkkeluar`. Defaults to None.
            jenis_gtk (Optional[str], optional): antara `guru` dan `tendik`. Defaults to None.
            limit (int, optional): batas data yang dikembalikan. Defaults to 25.
            penugasan_null (Optional[int], optional): Tambpilkan data dengan penugasan kosong. Defaults to None.
            page (int, optional): Halaman data. Defaults to 1.
            start (int, optional): Mulai dari. Defaults to 0.

        Returns:
            List[Ptk]: List dari data Ptk
        """
        query = self._query(
            entry_sekolah_id=sekolah_id,
            ptk_module=ptk_module,
            tahun_ajaran_id=tahun_ajaran_id,
            jenis_gtk=jenis_gtk,
            limit=limit,
            penugasan_null=penugasan_null,
            page=page,
            start=start,
        )
        return self._get_rest(
            path="ptk" if ptk_module == "ptkkeluar" else "Ptk",
            cl=List[Ptk],
            query=query,
            prefix="customrest/" if ptk_module == "ptkkeluar" else "rest/",
        )

    guru = partialmethod(
        ptk,
        ptk_module="ptkterdaftar",
        jenis_gtk="guru",
        penugasan_null=2,
    )

    tendik = partialmethod(
        ptk,
        ptk_module="ptkterdaftar",
        jenis_gtk="tendik",
        penugasan_null=2,
    )

    ptk_keluar = partialmethod(
        ptk,
        ptk_module="ptkkeluar",
    )

    def ptk_terdaftar(
        self,
        ptk_id: Optional[str] = None,
        sekolah_id: Optional[str] = None,
        tahun_ajaran_id: Optional[str] = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[PtkTerdaftar]:
        """ptk_terdaftar mengambil data PtkTerdaftar

        Args:
            ptk_id (Optional[str], optional): ID milik Ptk. Defaults to None.
            sekolah_id (Optional[str], optional): Sekolah ID. Defaults to None.
            tahun_ajaran_id (Optional[str], optional): Tahun ajar ID. Defaults to None.
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Mulai dari. Defaults to 0.
            limit (int, optional): Batas data. Defaults to 50.

        Returns:
            List[PtkTerdaftar]: [description]
        """
        query = self._query(
            sekolah_id=sekolah_id,
            tahun_ajaran_id=tahun_ajaran_id,
            ptk_id=ptk_id,
            page=page,
            start=start,
            limit=limit,
        )
        return self._get_rest("PtkTerdaftar", List[PtkTerdaftar], query=query)
