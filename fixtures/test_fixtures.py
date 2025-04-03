import pytest 

@pytest.fixture
def sample_data():
    return {"name":"Ajjayya", "age":23, "role":"Developer"}

def test_check_name(sample_data):
    assert sample_data["name"] == "Ajjayya"

def test_check_age(sample_data):
    assert sample_data["age"]== 23


@pytest.fixture(scope="module")
def db_connection():
    print("Opening Database Connection")
    db = {"status":"Connected"}
    yield db
    print("Closing Database Connection")
    db["status"] = "disconnected"

def test_db_status(db_connection):
    assert db_connection["status"] == "Connected"


def test_db_status_again(db_connection):
    assert db_connection["status"] == "Connected"        