import pytest
import requests
import sqlite3
import os
from typing import Any
from utils.file_loader import load_json

BASE_URL = "https://fakestoreapi.com"
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/products.json"))["test_get_all_products"],
)
def test_get_all_products(db: sqlite3.Connection, case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/products", timeout=10)
    assert response.status_code == case["expected_status"]
    data = response.json()
    assert len(data) == case["expected_count"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/products.json"))["test_get_product_by_id"],
)
def test_get_product_by_id(db: sqlite3.Connection, case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/products/{case['id']}", timeout=10)
    assert response.status_code == case["expected_status"]
    data = response.json()
    assert data["id"] == case["id"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/products.json"))[
        "test_get_products_by_category"
    ],
)
def test_get_products_by_category(db: sqlite3.Connection, case: dict[str, Any]):
    response = requests.get(
        f"{BASE_URL}/products?category={case['category']}", timeout=10
    )
    assert response.status_code == case["expected_status"]
    data = response.json()
    assert any(product["category"] == case["category"] for product in data)


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/products.json"))["test_create_product"],
)
def test_create_product(db: sqlite3.Connection, case: dict[str, Any]):
    new_product = case["input"]
    response = requests.post(f"{BASE_URL}/products", json=new_product, timeout=10)
    assert response.status_code == case["expected_status"]
    data = response.json()
    assert data["title"] == new_product["title"]
    assert data["price"] == new_product["price"]
    assert data["category"] == new_product["category"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/products.json"))["test_update_product"],
)
def test_update_product(db: sqlite3.Connection, case: dict[str, Any]):
    updated_product = case["input"]
    response = requests.put(
        f"{BASE_URL}/products/{case['id']}", json=updated_product, timeout=10
    )
    data = response.json()

    assert response.status_code == case["expected_status"]
    assert data["title"] == updated_product["title"]
    assert data["price"] == updated_product["price"]
    assert data["category"] == updated_product["category"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/products.json"))["test_delete_product"],
)
def test_delete_product(db: sqlite3.Connection, case: dict[str, Any]):
    response = requests.delete(f"{BASE_URL}/products/{case['id']}", timeout=10)
    assert response.status_code == case["expected_status"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/products.json"))[
        "test_performance_get_all_products"
    ],
)
def test_performance_get_all_products(db: sqlite3.Connection, case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/products", timeout=10)
    assert response.status_code == case["expected_status"]
    assert response.elapsed.total_seconds() * 1000 < case["max_response_time_ms"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/products.json"))[
        "test_performance_get_product_by_id"
    ],
)
def test_performance_get_product_by_id(db: sqlite3.Connection, case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/products/{case['id']}", timeout=10)
    assert response.status_code == case["expected_status"]
    assert response.elapsed.total_seconds() * 1000 < case["max_response_time_ms"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/products.json"))[
        "test_performance_create_product"
    ],
)
def test_performance_create_product(db: sqlite3.Connection, case: dict[str, Any]):
    new_product: dict[str, Any] = case["input"]
    response = requests.post(f"{BASE_URL}/products", json=new_product, timeout=10)
    assert response.status_code == case["expected_status"]
    assert response.elapsed.total_seconds() * 1000 < case["max_response_time_ms"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/products.json"))["test_db_validation"],
)
def test_db_validation(db: sqlite3.Connection, case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/products", timeout=10)
    assert response.status_code == case["expected_status"]
    data = response.json()
    api_count = len(data)

    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM products")
    db_count = cursor.fetchone()[0]

    assert api_count == db_count


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    load_json(os.path.join(BASE_DIR, "data/products.json"))["test_invalid_url"],
)
def test_invalid_url(case: dict[str, Any]):
    response = requests.get(f"{BASE_URL}/products/{case['url']}", timeout=10)
    assert response.status_code == case["expected_status"]
