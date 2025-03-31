'''

IN Pytest Assertions are the  primary way to test  conditions, Python's built in assert statement 
is used to compare expected and actual outcomes , if assertion fails ,pytest provides a detailed failure report

'''
import pytest

#Basic Assertions in pytest

def test_add():
    assert 2 + 3 == 5
    assert 5 + 2 == 7


def test_example():
    a = 5
    b = 10
    # assert a > b
    # assert b > a


def  test_subtract():
    result =  10 - 5
    assert result == 5 , "Expected  result is 5 , but  got 4 "


