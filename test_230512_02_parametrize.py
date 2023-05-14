import pytest


@pytest.mark.parametrize(
    argnames="x,y",
    argvalues=[
        (0, 0),
        (0, 1)],
    ids=["TEST_01_PASS", "TEST_02_FAIL"])
def test_1(x, y):
    """ Parametetrized """
    assert x == y
