from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_docs():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    result = client.get(
        "/health"
    )
    assert result.status_code == 200
    assert result.json()[0]['status'] == 'True'


def test_health():
    result = client.post(
        "/health"
    )
    assert result.status_code == 405


def test_detect_lang():
    result = client.post(
        "/detect_language",
        json={"text": "Campa cavallo che l erba cresce"},
    )
    assert result.status_code == 200
    assert result.json()[0]['lang'] == 'it'
