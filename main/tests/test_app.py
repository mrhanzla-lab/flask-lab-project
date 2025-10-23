import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Flask Lab Project" in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b"OK" in response.data

def test_post_data(client):
    payload = {"name": "tester"}
    response = client.post('/data', json=payload)
    assert response.status_code == 201
    body = response.get_json()
    assert body["received"]["name"] == "tester"