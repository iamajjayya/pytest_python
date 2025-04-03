import pytest

@pytest.fixture(scope="class")
def class_data():
    return {"framework":"pytest","language":"Python"}

class TestFramework:
    def test_frmework(self, class_data):
        assert class_data["framework"] == "pytest"

    def test_language(self, class_data):
        assert class_data["language"] == "Python"    


