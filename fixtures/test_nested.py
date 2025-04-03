import pytest

@pytest.fixture
def db_connection():
    return {"db":"Mysql", "status":"connected"}

@pytest.fixture
def user_data(db_connection):
    return {"username":"admin" ,"db":db_connection}

def test_user_db(user_data):
    assert user_data["db"]["status"] == "connected"

    
