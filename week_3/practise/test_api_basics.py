import requests
from typing import Any

URL = "https://jsonplaceholder.typicode.com"


def test_get_users():
    response = requests.get(f"{URL}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "name" in response.json()[0]
    assert "email" in response.json()[0]


def test_create_post():
    payload: dict[str, Any] = {
        "title": "Test Post",
        "body": "This is a test",
        "userId": 1,
    }
    response = requests.post(f"{URL}/posts", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["title"] == payload["title"]
