from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("api/health")
    assert response.status_code == 200
