import os
import uuid
import pytest
import requests
from typing import Any


@pytest.fixture(scope="session")
def base_url():
    return "https://gorest.co.in/public/v2"


@pytest.fixture(scope="session")
def api_token():
    return os.getenv("BEARER_TOKEN_GOREST")


@pytest.fixture(scope="session")
def auth_headers(api_token: str):
    return {"Authorization": f"Bearer {api_token}"}


@pytest.fixture(scope="function")
def api_client(auth_headers: dict[str, Any]):
    session = requests.Session()
    session.headers.update(auth_headers)
    return session


@pytest.fixture(scope="function")
def created_user(api_client: requests.Session, base_url: str):
    unique_email = f"bunny_{uuid.uuid4().hex[:8]}@email.com"
    payload = {
        "name": "Bunny",
        "email": unique_email,
        "gender": "male",
        "status": "active",
    }
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    assert response.status_code == 201, f"Failed to create user: {response.text}"
    user_data = response.json()

    yield user_data

    api_client.delete(f"{base_url}/users/{user_data['id']}")
