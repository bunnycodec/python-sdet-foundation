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
    load_json(os.path.join(BASE_DIR, "data/carts.json"))["test_get_all_carts"],
)
def test_get_all_carts(case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/carts", timeout=10)
    assert response.status_code == case["expected_status"]

    data = response.json()
    assert len(data) == case["expected_count"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/carts.json"))["test_get_cart_by_id"],
)
def test_get_cart_by_id(case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/carts/{case['id']}", timeout=10)
    assert response.status_code == case["expected_status"]
    data = response.json()
    assert data["userId"] == case["expected_user_id"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/carts.json"))["test_create_cart"],
)
def test_create_cart(case: dict[str, Any]):
    payload = {"userId": case["user_id"], "products": case["products"]}
    response = requests.post(f"{BASE_URL}/carts", json=payload, timeout=10)
    assert response.status_code == case["expected_status"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/carts.json"))["test_update_cart"],
)
def test_update_cart(case: dict[str, Any]):
    payload = {"userId": case["user_id"], "products": case["products"]}
    response = requests.put(f"{BASE_URL}/carts/{case['id']}", json=payload, timeout=10)
    assert response.status_code == case["expected_status"]
    data = response.json()
    assert data["userId"] == case["user_id"]
    assert data["products"] == case["products"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/carts.json"))["test_delete_cart"],
)
def test_delete_cart(case: dict[str, Any]):
    response = requests.delete(f"{BASE_URL}/carts/{case['id']}", timeout=10)
    assert response.status_code == case["expected_status"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/carts.json"))[
        "test_get_cart_by_id_not_found"
    ],
)
def test_get_cart_by_id_not_found(case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/carts/{case['id']}", timeout=10)
    assert response.status_code == case["expected_status"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/carts.json"))[
        "test_performance_get_all_carts"
    ],
)
def test_performance_get_all_carts(case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/carts", timeout=10)
    assert response.status_code == case["expected_status"]
    assert response.elapsed.total_seconds() * 1000 < case["max_response_time"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/carts.json"))[
        "test_performance_get_cart_by_id"
    ],
)
def test_performance_get_cart_by_id(case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/carts/{case['id']}", timeout=10)
    assert response.status_code == case["expected_status"]
    assert response.elapsed.total_seconds() * 1000 < case["max_response_time"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/carts.json"))[
        "test_performance_create_cart"
    ],
)
def test_performance_create_cart(case: dict[str, Any]):
    payload = {"userId": case["user_id"], "products": case["products"]}
    response = requests.post(f"{BASE_URL}/carts", json=payload, timeout=10)
    assert response.status_code == case["expected_status"]
    assert response.elapsed.total_seconds() * 1000 < case["max_response_time"]
