import pytest


@pytest.fixture
def readfile():
    with open("file_test.txt") as f:
        return f.read()


def test(readfile: str):
    """ fixture を引数にとる """
    assert readfile == 'yuri_ebihara'
