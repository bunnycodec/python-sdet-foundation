import pytest
import requests
from typing import Any


@pytest.mark.smoke
def test_no_auth_token_create_user(base_url: str):
    payload: dict[str, str] = {
        "name": "Bunny",
        "email": "someemail@email.com",
        "gender": "male",
        "status": "active",
    }
    response = requests.post(f"{base_url}/users", json=payload, timeout=10)
    assert response.status_code == 401


@pytest.mark.smoke
def test_create_user_invalid_token_401(base_url: str):
    payload: dict[str, str] = {
        "name": "Bunny",
        "email": "someemail@email.com",
        "gender": "male",
        "status": "active",
    }
    headers = {"Authorization": "Bearer invalidcode"}
    response = requests.post(
        f"{base_url}/users", json=payload, headers=headers, timeout=10
    )
    assert response.status_code == 401


@pytest.mark.smoke
def test_delete_user_no_auth_401(base_url: str):
    response = requests.delete(f"{base_url}/users/99999", timeout=10)
    assert response.status_code == 401


@pytest.mark.smoke
def test_missing_email_422(api_client: requests.Session, base_url: str):
    payload: dict[str, str] = {
        "name": "Bunny",
        "gender": "male",
        "status": "inactive",
    }
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    error_data = response.json()

    assert response.status_code == 422
    assert any("email" in str(err).lower() for err in error_data)


@pytest.mark.smoke
def test_missing_name_422(api_client: requests.Session, base_url: str):
    payload: dict[str, str] = {
        "email": "Bunny@email.com",
        "gender": "male",
        "status": "inactive",
    }
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    error_data = response.json()

    assert response.status_code == 422
    assert any("name" in str(err).lower() for err in error_data)


@pytest.mark.smoke
def test_missing_user_id_422(api_client: requests.Session, base_url: str):
    payload: dict[str, Any] = {
        "title": "bunny title",
        "body": "dummy body",
    }
    response = api_client.post(f"{base_url}/posts", json=payload, timeout=10)
    error_data = response.json()

    assert response.status_code == 422
    assert any("user_id" in str(err).lower() for err in error_data)


@pytest.mark.smoke
def test_invalid_email_422(api_client: requests.Session, base_url: str):
    payload: dict[str, str] = {
        "name": "Bunny",
        "gender": "male",
        "email": "something invalid",
        "status": "inactive",
    }
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    error_data = response.json()

    assert response.status_code == 422
    assert any("email" in str(err).lower() for err in error_data)


@pytest.mark.smoke
def test_non_integer_user_id_422(api_client: requests.Session, base_url: str):
    payload: dict[str, Any] = {
        "user_id": "bunny",
        "title": "fake title",
        "body": "fake body",
    }
    response = api_client.post(f"{base_url}/posts", json=payload, timeout=10)
    error_data = response.json()

    assert response.status_code == 422
    assert any("is not a number" in str(err).lower() for err in error_data)


@pytest.mark.smoke
def test_get_non_existent_user_404(api_client: requests.Session, base_url: str):
    response = api_client.get(f"{base_url}/users/99999", timeout=10)
    error_data = response.json()

    assert response.status_code == 404
    assert "resource not found" in str(error_data).lower()


@pytest.mark.smoke
def test_update_non_existent_user_404(api_client: requests.Session, base_url: str):
    payload = {"name": "Bunny Updated"}
    response = api_client.patch(f"{base_url}/users/99999", json=payload, timeout=10)
    error_data = response.json()

    assert response.status_code == 404
    assert "resource not found" in str(error_data).lower()
