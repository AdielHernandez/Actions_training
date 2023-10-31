from training import *

list1 = [2,5,6,1]
list_ans = [1,2,5,6]
def test_sort():
    assert sortArr(list1) == list_ans

def test_sum():
    assert sum(5,5) == 45