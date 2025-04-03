import pytest 

def test_project_name(global_data):
    assert global_data["project"] == "Test Suite"