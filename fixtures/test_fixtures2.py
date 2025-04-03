
import pytest

@pytest.fixture(params=[(2,3,5),(4,5,9),(1,2,3)])
def add_data(request):
    return request.param

def test_addition(add_data):
    x,y,expected = add_data
    assert x + y == expected 