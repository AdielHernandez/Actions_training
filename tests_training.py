#unit tests with pytests
from training import *

#unsorted list
list1 = [2,5,6,1]

#expected output of sorted list
list_ans = [1,2,5,6]

#test sort function
def test_sort():
    assert sortArr(list1) == list_ans

#test sum function
def test_sum():
    assert sum(5,5) == 10