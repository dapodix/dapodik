import os
from dapodik import Dapodik, __semester__
from dotenv import load_dotenv
from pytest import fixture

load_dotenv()

USERNAME = os.environ.get("USERNAME", "")
PASSWORD = os.environ.get("PASSWORD", "")
SEMESTER_ID = os.environ.get("SEMESTER_ID", __semester__)
SERVER = os.environ.get("SERVER", "http://localhost:5774/")


@fixture
def dapodik() -> Dapodik:
    return Dapodik(
        username=USERNAME,
        password=PASSWORD,
        semester_id=SEMESTER_ID,
        server=SERVER,
    )
