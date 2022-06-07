from os import lseek

from app.main import main


def test_main():
    assert main() == 0
