from client.api_client import get, post
from typing import List, Dict, Any
from assertions.response_assertions import (assert_status_code, assert_json_has_keys, assert_json_field_equals)


def test_get_posts_with_query_params():
    response = get("/posts", {"userId": 3})

    assert_status_code(response, 200)

    data: List[Dict[str, Any]] = response.json()
    assert isinstance(data, list)

    for item in data:
        assert item["userId"] == 3, f"Expected userId was 3 but got {item['userId']}"

def test_get_single_post_valid_id():
    response = get("/posts/1")
    keys = {"id", "userId", "title", "body"}

    assert_status_code(response, 200)
    assert_json_has_keys(response, keys)

def test_create_post_valid_payload():
    payload: dict[str, str|int] = {
        "userId": 1,
        "title": "SK_Testing",
        "body": "This is just a dummy testing done by SK"
    }

    response = post("/posts", payload)

    assert response.status_code == 201
    assert_status_code(response, 201)
    assert_json_field_equals(response, "title", payload["title"])

def test_get_post_invalid_id():
    response = get("/posts/9999")

    assert_status_code(response, 404)

def test_create_post_empty_payload():
    payload: dict[str, Any] = {}
    response = post("/posts", payload)

    assert_status_code(response, 201)

def test_post_response_structure():
    response = get("/posts/1")
    keys = {"id", "userId", "title", "body"}

    assert_status_code(response, 200)
    assert_json_has_keys(response, keys)
    