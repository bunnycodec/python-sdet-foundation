from typing import Any
import requests
import pytest
import os

URL = "https://gorest.co.in/public/v2"


@pytest.fixture
def auth_headers():
    return {"Authorization": f"Bearer {os.getenv("BEARER_TOKEN_GOREST")}"}


def test_get_users_with_bearer_token(auth_headers: dict[str, Any]):
    response = requests.get(f"{URL}/users", headers=auth_headers)

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "name" in response.json()[0]
    assert "email" in response.json()[0]
