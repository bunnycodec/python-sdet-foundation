import requests
import pytest


@pytest.mark.smoke
def test_create_user_missing_required_field(
    api_client: requests.Session, base_url: str
):
    payload = {
        "name": "Bunny",
        "gender": "male",
        "status": "active",
    }
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    data = response.json()

    assert response.status_code == 422
    assert any("email" in str(err).lower() for err in data)
    assert any(err["message"] == "can't be blank" for err in data)


@pytest.mark.smoke
def test_create_user_invalid_email_format(api_client: requests.Session, base_url: str):
    payload = {
        "name": "Bunny",
        "email": "dummy-email-invalid",
        "gender": "male",
        "status": "active",
    }
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    data = response.json()

    assert response.status_code == 422
    assert any("email" in str(err).lower() for err in data)
    assert any(err["message"] == "is invalid" for err in data)


@pytest.mark.smoke
def test_create_user_invalid_gender(api_client: requests.Session, base_url: str):
    payload = {
        "name": "Bunny",
        "email": "bunny@test.com",
        "gender": "testing",
        "status": "active",
    }
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    data = response.json()

    assert response.status_code == 422
    assert any("gender" in str(err).lower() for err in data)
    assert any(
        err["message"] == "can't be blank, can be male of female" for err in data
    )


@pytest.mark.smoke
def test_get_nonexistent_user(api_client: requests.Session, base_url: str):
    response = api_client.get(f"{base_url}/users/999999", timeout=10)

    assert response.status_code == 404
    assert response.json()["message"] == "Resource not found"


@pytest.mark.smoke
def test_update_nonexistent_user(api_client: requests.Session, base_url: str):
    payload = {"name": "Bunny Updated"}
    response = api_client.patch(f"{base_url}/users/999999", json=payload, timeout=10)

    assert response.status_code == 404


@pytest.mark.smoke
def test_delete_nonexistent_user(api_client: requests.Session, base_url: str):
    response = api_client.delete(f"{base_url}/users/999999", timeout=10)

    assert response.status_code == 404


@pytest.mark.smoke
def test_unauthorized_access(base_url: str):
    payload = {
        "name": "Test",
        "email": "test@example.com",
        "gender": "male",
        "status": "active",
    }
    response = requests.post(f"{base_url}/users", json=payload, timeout=10)

    assert response.status_code == 401
