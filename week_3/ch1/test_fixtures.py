import uuid
import requests


def test_get_users(api_client: requests.Session, base_url: str):
    response = api_client.get(f"{base_url}/users", timeout=10)
    assert response.status_code == 200


def test_create_user(api_client: requests.Session, base_url: str):
    unique_email = f"bunny_{uuid.uuid4().hex[:8]}@email.com"
    payload = {
        "name": "Bunny",
        "email": unique_email,
        "gender": "male",
        "status": "active",
    }
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    assert response.status_code == 201
    assert response.json()["email"] == unique_email
