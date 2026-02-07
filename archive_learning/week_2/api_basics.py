from typing import Any
import requests

Base_URL = "https://jsonplaceholder.typicode.com"

def get_posts_with_query_params():
    params = {"userId": 3}
    response = requests.get(f"{Base_URL}/posts", params=params)

    print(f"Status Code: {response.status_code}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def get_single_post_and_validate_json():
    response = requests.get(f"{Base_URL}/posts/2")
    response_json = response.json()
    
    assert response.status_code == 200
    assert response_json["id"] == 2
    assert "body" in response_json
    assert "title" in response_json

def create_post_with_payload():
    payload: dict[str, Any] = {
        "userId": 1,
        "title": "SK_Testing",
        "body": "This is just a dummy testing done by SK"
    }

    response = requests.post(f"{Base_URL}/posts", json=payload)

    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]


if __name__ == "__main__":
    get_posts_with_query_params()
    get_single_post_and_validate_json()
    create_post_with_payload()
