from dapodik.__main__ import main
from dapodik.main import main as main_main


def test_main():
    assert callable(main)
    assert callable(main_main)
    assert main is main_main
