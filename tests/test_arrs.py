import  pytest
from pytest_proj.utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3, 5 ,2], 3) == 5
    assert arrs.get([0], 0) == 0
    assert arrs.get([1, 2, 3], 0,1) == 1
    assert arrs.get([1, 2, 3], -1, "test") == "test"
    assert arrs.get([], -1, "test") == "test"
    assert arrs.get(["1","2"], 1, "test") == "2"
    assert arrs.get([True, "2"], 0, "test") == True
    assert arrs.get(["test"], 0, "test") == "test"


def test_indexerror():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")
        arrs.get([], 1)
def test_TypeError():
    with pytest.raises(TypeError):
         arrs.get([1, 2, 3, 5, 2], " ")
         arrs.get([1, 2, 3, 5, 2], 0.0)
         arrs.get(1, 0, 1)
def test_AssertionError():
    with pytest.raises(AssertionError):
        assert arrs.get([1, 2, 3], 1, "test")
        assert arrs.get([1, 2, 3, 5, 2], 3) == 2
        assert arrs.get([1, 2, 3], 0) == 1.5
        assert arrs.get([1, 2, 3], 1, 1) == "2.0"
        assert arrs.get([1, 2, 3], 1, 1) == -1

def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1,2,3,4,5,6], -1,-1) == []
    assert arrs.my_slice([0,1,2,3],-6) == [0, 1, 2, 3]









def test_typeer_myslice():
    with pytest.raises(TypeError):
        arrs.my_slice([1, 2, 3, 4], 0, "")
        arrs.my_slice([1, 2, 3, 4], 0, 0.0)
        arrs.my_slice(0,0,0)
