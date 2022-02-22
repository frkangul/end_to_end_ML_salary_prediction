"""
pytest api_test.py -vv
"""
import pytest
from api import app
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def client():
    client_tc = TestClient(app)
    return client_tc


def test_get(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"msg": "Welcome salary prediction application"}


def test_post_belove(client):
    req = {
        "age": 20,
        "workclass": "State-gov",
        "education": "Bachelors",
        "marital_status": "Never-married",
        "occupation": "Adm-clerical",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "hours_per_week": 20,
        "native_country": "United-States"
    }
    r = client.post("/", json=req)
    assert r.status_code == 200
    assert r.json() == {"prediction": "<=50K"}


def test_post_above(client):
    req = {
          "age": 41,
          "workclass": "Private",
          "education": "Masters",
          "marital_status": "Married-civ-spouse",
          "occupation": "Exec-managerial",
          "relationship": "Not-in-family",
          "race": "White",
          "sex": "Male",
          "hours_per_week": 65,
          "native_country": "United-States"
    }
    r = client.post("/", json=req)
    assert r.status_code == 200
    assert r.json() == {"prediction": ">50K"}
