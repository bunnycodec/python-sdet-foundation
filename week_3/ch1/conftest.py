import os
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
