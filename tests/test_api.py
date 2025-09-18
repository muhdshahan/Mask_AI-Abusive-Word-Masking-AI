# integration tests for FastAPI endpoints

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_detect_clean_text():
    response = client.post("/detect", json={"text": "Hello friend", "threshold": 0.5})
    assert response.status_code == 200
    data = response.json()
    assert data["is_toxic"] is False
    assert data["cleaned_text"] == "Hello friend"


def test_detect_toxic_test():
    response = client.post("/detect", json={"text": "I will kill you", "threshold": 0.5})
    assert response.status_code == 200
    data = response.json()
    assert data["is_toxic"] is True
    assert "*" in data["cleaned_text"]


