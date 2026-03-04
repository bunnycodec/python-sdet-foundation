import pytest
import requests
import os
from typing import Any
from utils.file_loader import load_json

BASE_URL = "https://fakestoreapi.com"
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/users.json"))["test_get_all_users"],
)
def test_get_all_users(case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/users", timeout=10)
    assert response.status_code == case["expected_status"]
    data = response.json()
    assert len(data) == case["expected_count"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/users.json"))["test_get_user_by_id"],
)
def test_get_user_by_id(case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/users/{case['id']}", timeout=10)
    assert response.status_code == case["expected_status"]
    data = response.json()
    name = data["name"]["firstname"] + " " + data["name"]["lastname"]
    assert name == case["expected_name"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/users.json"))["test_create_user"],
)
def test_create_user(case: dict[str, Any]):
    payload = {"username": case["username"], "email": case["email"]}
    response = requests.post(f"{BASE_URL}/users", json=payload, timeout=10)
    assert response.status_code == case["expected_status"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/users.json"))["test_update_user"],
)
def test_update_user(case: dict[str, Any]):
    payload = {"username": case["username"], "email": case["email"]}
    response = requests.put(f"{BASE_URL}/users/{case['id']}", json=payload, timeout=10)
    assert response.status_code == case["expected_status"]
    data = response.json()
    assert data["username"] == case["username"]
    assert data["email"] == case["email"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/users.json"))["test_delete_user"],
)
def test_delete_user(case: dict[str, Any]):
    response = requests.delete(f"{BASE_URL}/users/{case['id']}", timeout=10)
    assert response.status_code == case["expected_status"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/users.json"))["test_get_nonexistent_user"],
)
def test_get_nonexistent_user(case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/users/{case['id']}asdfsd", timeout=10)
    assert response.status_code == case["expected_status"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/users.json"))["test_invalid_url_for_user"],
)
def test_invalid_url_for_user(case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/users/{case['url']}", timeout=10)
    print(response.json())
    assert response.status_code == case["expected_status"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/users.json"))[
        "test_performance_get_all_users"
    ],
)
def test_performance_get_all_users(case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/users", timeout=10)
    assert response.status_code == case["expected_status"]
    assert response.elapsed.total_seconds() * 1000 < case["max_response_time"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/users.json"))[
        "test_performance_get_user_by_id"
    ],
)
def test_performance_get_user_by_id(case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/users/{case['id']}", timeout=10)
    assert response.status_code == case["expected_status"]
    assert response.elapsed.total_seconds() * 1000 < case["max_response_time"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/users.json"))[
        "test_performance_create_user"
    ],
)
def test_performance_create_user(case: dict[str, Any]):
    payload = {"username": case["username"], "email": case["email"]}
    response = requests.post(f"{BASE_URL}/users", json=payload, timeout=10)
    assert response.status_code == case["expected_status"]
    assert response.elapsed.total_seconds() * 1000 < case["max_response_time"]
