'Fixtures can be automatically applied to every test without expliciting calling them'
import pytest

@pytest.fixture(autouse=True)
def log_test_executtion():
    print("\n Test is Starting")
    yield
    print("\n Test finished")


def test_example():
    assert 1 +  1== 2
        