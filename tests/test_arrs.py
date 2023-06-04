import  pytest
from pytest_proj.utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 5, 3], 1, "test") == 5
    assert arrs.get([1, 2, 3,5,6,2], 2, "test") == 3

def test_indexerror():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
