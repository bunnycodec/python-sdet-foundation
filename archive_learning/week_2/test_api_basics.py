import requests

Base_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_with_query_params():
    params = {"userId": 3}
    response = requests.get(f"{Base_URL}/posts", params=params)

    assert response.status_code == 200
    assert isinstance(response.json(), list)

    for post in response.json():
        assert post["userId"] == 3

def test_get_single_post_valid_id():
    response = requests.get(f"{Base_URL}/posts/1")
    keys = {"id", "userId", "title", "body"}

    assert response.status_code == 200
    assert keys.issubset(response.json())

def test_create_post_valid_payload():
    payload: dict[str, str|int] = {
        "userId": 1,
        "title": "SK_Testing",
        "body": "This is just a dummy testing done by SK"
    }

    response = requests.post(f"{Base_URL}/posts", json=payload)

    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]

def test_get_post_invalid_id():
    response = requests.get(f"{Base_URL}/posts/9999")

    assert response.status_code == 404

def test_create_post_empty_payload():
    payload: dict[str, str] = {}
    response = requests.post(f"{Base_URL}/posts", json=payload)

    assert response.status_code == 201

def test_post_response_structure():
    response = requests.get(f"{Base_URL}/posts/1")
    keys = {"id", "userId", "title", "body"}
    data = response.json()

    assert response.status_code == 200
    assert keys.issubset(data.keys())
    