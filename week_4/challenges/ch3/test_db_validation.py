import pytest
import json
import os
import sqlite3
import requests

BASE_URL = "https://fakestoreapi.com"


def load_json(filepath: str):
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, filepath)
    with open(full_path) as file:
        return json.load(file)


@pytest.mark.smoke
@pytest.mark.parametrize("case", load_json("data/seeds.json")["count_products"])
def test_count_products(case: dict[str, int], db: sqlite3.Connection):
    response = requests.get(f"{BASE_URL}/products", timeout=10)

    assert response.status_code == case["expected_status"]

    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM products")
    db_count = cursor.fetchone()[0]
    assert len(response.json()) == db_count


@pytest.mark.smoke
@pytest.mark.parametrize("case", load_json("data/seeds.json")["product_validate"])
def test_product_validate(case: dict[str, int], db: sqlite3.Connection):
    response = requests.get(f"{BASE_URL}/products/{case['id']}", timeout=10)
    product = response.json()

    assert response.status_code == case["expected_status"]

    cursor = db.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product["id"],))
    db_product = cursor.fetchone()
    assert db_product is not None
    assert product["id"] == db_product[0]
    assert product["title"] == db_product[1]
    assert product["price"] == db_product[2]
    assert product["category"] == db_product[3]


@pytest.mark.smoke
@pytest.mark.parametrize("case", load_json("data/seeds.json")["product_category"])
def test_product_category(case: dict[str, int], db: sqlite3.Connection):
    response = requests.get(
        f"{BASE_URL}/products/category/{case['category']}", timeout=10
    )
    products = response.json()

    assert response.status_code == case["expected_status"]
    assert all(product["category"] == case["category"] for product in products)

    # check if this category exists in the database
    cursor = db.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM products WHERE category = ?", (case["category"],)
    )
    db_count = cursor.fetchone()[0]
    assert db_count > 0
