import requests
import pytest
import json
import os
from typing import Any

BASE_URL = "https://fakestoreapi.com"


class ProductBuilder:
    def __init__(self) -> None:
        self._product: dict[str, Any] = {
            "title": "Test Product",
            "price": 9.99,
            "category": "electronics",
            "description": "test description",
        }

    def with_title(self, new_title: str) -> "ProductBuilder":
        self._product["title"] = new_title
        return self

    def with_price(self, new_price: float) -> "ProductBuilder":
        self._product["price"] = new_price
        return self

    def with_category(self, new_category: str) -> "ProductBuilder":
        self._product["category"] = new_category
        return self

    def with_description(self, new_description: str) -> "ProductBuilder":
        self._product["description"] = new_description
        return self

    def build(self) -> dict[str, Any]:
        return self._product


def load_json(filepath: str) -> Any:
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, filepath)
    with open(full_path) as file:
        return json.load(file)


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case", load_json("data/products.json")["get_products_with_limit"]
)
def test_products_with_limits(case: dict[str, str]):
    response = requests.get(f"{BASE_URL}/products?limit={case['limit']}", timeout=10)

    assert response.status_code == case["expected_status"]
    assert len(response.json()) == case["expected_count"]


@pytest.mark.smoke
@pytest.mark.parametrize("case", load_json("data/products.json")["get_product_by_id"])
def test_products_with_id(case: dict[str, str]):
    response = requests.get(f"{BASE_URL}/products/{case["product_id"]}", timeout=10)

    assert response.status_code == case["expected_status"]
    assert response.json()["id"] == case["product_id"]


@pytest.mark.smoke
@pytest.mark.parametrize("case", load_json("data/products.json")["get_categories"])
def test_products_get_categories(case: dict[str, str]):
    response = requests.get(f"{BASE_URL}/products/categories", timeout=10)

    assert response.status_code == case["expected_status"]


@pytest.mark.smoke
def test_default_payload():
    product = ProductBuilder().build()

    assert product["title"] == "Test Product"
    assert product["price"] == 9.99
    assert product["category"] == "electronics"
    assert product["description"] == "test description"


@pytest.mark.smoke
def test_expensive_product():
    product = ProductBuilder().with_price(777.45).build()

    assert product["price"] > 500


@pytest.mark.smoke
def test_invalid_price_type():
    product = ProductBuilder().with_price("not_a_price").build()  # type: ignore

    assert isinstance(product["price"], str)
