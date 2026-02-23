import requests
import uuid
from typing import Any


def test_create_user(api_client: requests.Session, base_url: str):
    unique_email = f"bunny_{uuid.uuid4().hex[:8]}@codec.com"
    payload = {
        "name": "Bunny",
        "email": unique_email,
        "gender": "male",
        "status": "inactive",
    }
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    data = response.json()

    assert response.status_code == 201
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert data["gender"] == payload["gender"]

    api_client.delete(f"{base_url}/users/{data['id']}", timeout=10)


def test_read_user(
    api_client: requests.Session, base_url: str, created_user: dict[str, Any]
):
    user_id = created_user["id"]
    response = api_client.get(f"{base_url}/users/{user_id}", timeout=10)
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == created_user["id"]
    assert data["email"] == created_user["email"]
    assert data["name"] == created_user["name"]


def test_update_user(
    api_client: requests.Session, base_url: str, created_user: dict[str, Any]
):
    payload = {"name": "Bunny Updated"}
    user_id = created_user["id"]
    response = api_client.patch(f"{base_url}/users/{user_id}", json=payload, timeout=10)
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == payload["name"]

    # Verify persistence
    response = api_client.get(f"{base_url}/users/{user_id}", timeout=10)
    assert response.status_code == 200
    assert response.json()["name"] == payload["name"]


def test_delete_user(api_client: requests.Session, base_url: str):
    unique_email = f"bunny_{uuid.uuid4().hex[:8]}@codec.com"
    payload = {
        "name": "Bunny",
        "email": unique_email,
        "gender": "male",
        "status": "inactive",
    }

    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    assert response.status_code == 201, f"Failed to create user: {response.text}"

    user_id = response.json()["id"]
    response = api_client.delete(f"{base_url}/users/{user_id}")
    assert response.status_code == 204, f"Unable to delete the user: {response.text}"

    response = api_client.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 404


def test_full_crud_workflow(api_client: requests.Session, base_url: str):
    unique_email = f"bunny_{uuid.uuid4().hex[:8]}@codec.com"
    payload = {
        "name": "Bunny",
        "email": unique_email,
        "gender": "male",
        "status": "inactive",
    }

    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    assert response.status_code == 201, f"Failed to create user: {response.text}"

    user_id = response.json()["id"]
    response = api_client.get(f"{base_url}/users/{user_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]

    updated_payload = {"name": "Bunny_Patch"}
    response = api_client.patch(
        f"{base_url}/users/{user_id}", json=updated_payload, timeout=10
    )
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == updated_payload["name"]

    response = api_client.delete(f"{base_url}/users/{user_id}")
    assert response.status_code == 204, f"Unable to delete the user: {response.text}"

    response = api_client.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 404
