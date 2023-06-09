from series.series import fibonacci;
from series.series import lucas;

from series.series import sum_series;


def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected
 

def test_fibonacci_8():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected
 

def test_fibonacci_10():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected
 
def test_fibonacci_15():
    actual = fibonacci(15)
    expected = 610
    assert actual == expected
 

def test_lucas_1():

   actual = lucas(1)
   expected = 1
   assert actual == expected

def test_lucas_0():

   actual = lucas(0)
   expected = 2
   assert actual == expected



def test_lucas_5():

    actual = lucas(5)
    expected = 11 
    assert actual == expected


def test_lucas_10():

    actual = lucas(10)
    expected = 123 
    assert actual == expected

    

def test_sum_series_0():

    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_series_1():

    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_series_2():

    actual = sum_series(2)
    expected = 1
    assert actual == expected


def insertShiftArray(arr, val):
    mid = 0
    for i in arr:
        mid += 1
    mid = (mid - 1) // 2
    arr1 = arr[:]  
    for i in range(mid+1, mid+mid+2):
        arr[i] = arr1[i-1]  
    arr[mid] = val
    return arr


