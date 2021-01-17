import os
from dapodik import Dapodik, __semester__
from dotenv import load_dotenv
from pathlib import Path
from pytest import fixture

ROOT_PATH = Path("../../")
ENV_FILE_PATH = os.path.join(ROOT_PATH, ".env")
load_dotenv(ENV_FILE_PATH)

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
