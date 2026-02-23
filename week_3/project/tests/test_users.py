import requests
import pytest
import schemas
import uuid
from jsonschema import validate
from typing import Any


@pytest.mark.smoke
def test_create_user_201(api_client: requests.Session, base_url: str):
    unique_email = f"bunny_{uuid.uuid4().hex[:8]}@email.com"
    payload: dict[str, str] = {
        "name": "Bunny",
        "email": unique_email,
        "gender": "male",
        "status": "active",
    }
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    user_data = response.json()

    assert response.status_code == 201, f"Failed to create user: {response.text}"
    assert user_data["name"] == payload["name"]
    assert user_data["email"] == payload["email"]
    assert user_data["gender"] == payload["gender"]

    user_id = user_data["id"]
    api_client.delete(f"{base_url}/users/{user_id}", timeout=10)


@pytest.mark.smoke
def test_read_user_200(
    created_user: dict[str, Any], api_client: requests.Session, base_url: str
):
    user_id = created_user["id"]
    response = api_client.get(f"{base_url}/users/{user_id}", timeout=10)
    user_data = response.json()

    assert response.status_code == 200
    assert user_data["name"] == created_user["name"]
    assert user_data["email"] == created_user["email"]
    assert user_data["gender"] == created_user["gender"]


@pytest.mark.smoke
def test_update_user_name_200(
    created_user: dict[str, Any], api_client: requests.Session, base_url: str
):
    user_id = created_user["id"]
    payload = {"name": "Bunny Updated"}
    response = api_client.patch(f"{base_url}/users/{user_id}", json=payload, timeout=10)
    user_data = response.json()

    assert response.status_code == 200
    assert user_data["name"] == payload["name"]


@pytest.mark.smoke
def test_update_user_status_200(
    created_user: dict[str, Any], api_client: requests.Session, base_url: str
):
    user_id = created_user["id"]
    assert created_user["status"] == "active"
    payload = {"status": "inactive"}
    response = api_client.patch(f"{base_url}/users/{user_id}", json=payload, timeout=10)
    user_data = response.json()

    assert response.status_code == 200
    assert user_data["status"] == payload["status"]


@pytest.mark.smoke
def test_delete_user_204(api_client: requests.Session, base_url: str):
    unique_email = f"bunny_{uuid.uuid4().hex[:8]}@email.com"
    payload: dict[str, str] = {
        "name": "Bunny",
        "email": unique_email,
        "gender": "male",
        "status": "inactive",
    }
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    assert response.status_code == 201, f"User not created: {response.text}"

    user_id = response.json()["id"]
    response = api_client.delete(f"{base_url}/users/{user_id}", timeout=10)
    assert response.status_code == 204

    response = api_client.get(f"{base_url}/users/{user_id}", timeout=10)
    assert response.status_code == 404


@pytest.mark.smoke
def test_user_schema(
    created_user: dict[str, Any], api_client: requests.Session, base_url: str
):
    user_id = created_user["id"]
    response = api_client.get(f"{base_url}/users/{user_id}", timeout=10)
    user_data = response.json()

    validate(instance=user_data, schema=schemas.user_schema)


@pytest.mark.smoke
def test_user_list_schema(
    created_user: dict[str, Any], api_client: requests.Session, base_url: str
):
    response = api_client.get(f"{base_url}/users", timeout=10)
    user_data = response.json()

    validate(instance=user_data, schema=schemas.users_list_schema)


@pytest.mark.smoke
def test_create_user_schema(api_client: requests.Session, base_url: str):
    unique_email = f"bunny_{uuid.uuid4().hex[:8]}@email.com"
    payload: dict[str, str] = {
        "name": "Bunny",
        "email": unique_email,
        "gender": "male",
        "status": "inactive",
    }
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    user_data = response.json()

    validate(instance=user_data, schema=schemas.user_schema)
    user_id = user_data["id"]
    api_client.delete(f"{base_url}/users/{user_id}", timeout=10)


@pytest.mark.smoke
def test_pagination_validate_200(api_client: requests.Session, base_url: str):
    response = api_client.get(f"{base_url}/users?page=2", timeout=10)
    user_data = response.json()

    assert response.status_code == 200
    assert len(user_data) > 0


@pytest.mark.smoke
def test_status_active_validate_200(api_client: requests.Session, base_url: str):
    response = api_client.get(f"{base_url}/users?status=active", timeout=10)
    user_data = response.json()

    assert response.status_code == 200
    assert len(user_data) > 0
    assert all(user["status"] == "active" for user in user_data)


@pytest.mark.smoke
def test_status_inactive_validate_200(api_client: requests.Session, base_url: str):
    response = api_client.get(f"{base_url}/users?status=inactive", timeout=10)
    user_data = response.json()

    assert response.status_code == 200
    assert len(user_data) > 0
    assert all(user["status"] == "inactive" for user in user_data)


@pytest.mark.smoke
def test_gender_validate_200(api_client: requests.Session, base_url: str):
    response = api_client.get(f"{base_url}/users?gender=male", timeout=10)
    user_data = response.json()

    assert response.status_code == 200
    assert len(user_data) > 0
    assert all(user["gender"] == "male" for user in user_data)
