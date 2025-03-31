'''
Pytest.raises() isa feature in pytest that helps us check if a function correctly raises an error when
something goes wrong. This is usefull when testing how our program handles mistakes 


What Does pytest.raises() DO ?

it expects an error(exception) to happen , if the function does not a raise the exception the test fails 

Example :  Divinding by zero 



'''


import pytest

def divide(a,b):
    return a / b

def test_divide():
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide(10,0)

def add_numbers(a,b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        raise TypeError(" Input must be Numbers")
    return a + b

def test_add_numbers():
    with pytest.raises(TypeError):
        add_numbers("10",5)
        
