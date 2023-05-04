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


def test_sum_series_4():

    actual = sum_series(4)
    expected = 3
    assert actual == expected



def test_sum_series_8():

    actual = sum_series(8)
    expected = 21
    assert actual == expected


