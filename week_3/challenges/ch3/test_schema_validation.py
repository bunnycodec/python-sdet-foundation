import requests
import uuid
import schemas
from typing import Any
from jsonschema import validate


def test_single_user_schema(
    api_client: requests.Session, base_url: str, created_user: dict[str, Any]
):
    user_id = created_user["id"]
    response = api_client.get(f"{base_url}/users/{user_id}", timeout=10)
    validate(instance=response.json(), schema=schemas.user_schema)


def test_users_list_schema(api_client: requests.Session, base_url: str):
    response = api_client.get(f"{base_url}/users", timeout=10)
    validate(instance=response.json(), schema=schemas.user_list_schema)


def test_created_user_schema(api_client: requests.Session, base_url: str):
    unique_email = f"bunny_{uuid.uuid4().hex[:8]}@email.com"
    payload = {
        "name": "Bunny",
        "email": unique_email,
        "gender": "male",
        "status": "active",
    }
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    validate(instance=response.json(), schema=schemas.user_schema)

    user_id = response.json()["id"]
    api_client.delete(f"{base_url}/users/{user_id}", timeout=10)
