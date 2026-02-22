import requests
import pytest
import uuid
import os
from faker import Faker
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
    payload: dict[str, str] = {
        "name": "Bunny",
        "email": unique_email,
        "gender": "male",
        "status": "active",
    }
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    assert response.status_code == 201, f"Failed to create user: {response.text}"
    user_data = response.json()

    yield user_data

    api_client.delete(f"{base_url}/users/{user_data['id']}", timeout=10)


@pytest.fixture(scope="function")
def created_post(
    created_user: dict[str, Any], api_client: requests.Session, base_url: str
):
    fake = Faker()
    payload: dict[str, Any] = {
        "user_id": created_user["id"],
        "title": fake.sentence(nb_words=3),
        "body": fake.paragraph(nb_sentences=3),
    }
    response = api_client.post(f"{base_url}/posts", json=payload, timeout=10)
    assert response.status_code == 201, f"Failed to create Post: {response.text}"
    post_data = response.json()

    yield post_data

    api_client.delete(f"{base_url}/posts/{post_data['id']}", timeout=10)
