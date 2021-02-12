import os
import pytest
from dapodik import Dapodik, __semester__
from dapodik.sekolah import Sekolah
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.environ.get("USERNAME", "")
PASSWORD = os.environ.get("PASSWORD", "")
SEMESTER_ID = os.environ.get("SEMESTER_ID", __semester__)
SERVER = os.environ.get("SERVER", "http://localhost:5774/")


@pytest.fixture
def dapodik() -> Dapodik:
    return Dapodik(
        username=USERNAME,
        password=PASSWORD,
        semester_id=SEMESTER_ID,
        server=SERVER,
    )


@pytest.fixture
def sekolah(dapodik: Dapodik) -> Sekolah:
    return dapodik.sekolah()


@pytest.fixture
def sekolah_id(sekolah: Sekolah) -> str:
    return sekolah.sekolah_id


@pytest.fixture
def semester() -> str:
    return SEMESTER_ID
