import pytest
import os
import json
import requests
from typing import Any
from ch1.test_products import ProductBuilder

BASE_URL = "https://fakestoreapi.com"


def load_json(filepath: str):
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, filepath)
    with open(full_path) as file:
        return json.load(file)


@pytest.mark.smoke
@pytest.mark.parametrize("case", load_json("data/crud.json")["get_product"])
def test_get_all_products(case: dict[str, int]):
    response = requests.get(f"{BASE_URL}/products", timeout=10)

    assert response.status_code == case["expected_status"]


@pytest.mark.smoke
@pytest.mark.parametrize("case", load_json("data/crud.json")["create_product"])
def test_create_a_product(case: dict[str, Any]):
    payload_data: dict[str, Any] = case["payload"]
    payload = (
        ProductBuilder()
        .with_title(payload_data["title"])
        .with_category(payload_data["category"])
        .with_description(payload_data["description"])
        .with_price(payload_data["price"])
        .build()
    )
    response = requests.post(f"{BASE_URL}/products", json=payload, timeout=10)

    assert response.status_code == case["expected_status"]
    assert "id" in response.json()


@pytest.mark.smoke
@pytest.mark.parametrize("case", load_json("data/crud.json")["update_product"])
def test_update_a_product(case: dict[str, Any]):

    builder = ProductBuilder()

    if "title" in case:
        builder.with_title(case["title"])

    if "description" in case:
        builder.with_description(case["description"])

    if "category" in case:
        builder.with_category(case["category"])

    if "price" in case:
        builder.with_price(case["price"])

    payload = builder.build()

    response = requests.put(
        f"{BASE_URL}/products/{case['id']}", json=payload, timeout=10
    )

    assert response.status_code == case["expected_status"]
    for key in ["title", "description", "category", "price"]:
        if key in case:
            assert response.json()[key] == case[key]


@pytest.mark.smoke
@pytest.mark.parametrize("case", load_json("data/crud.json")["delete_product"])
def test_delete_a_product(case: dict[str, Any]):
    response = requests.delete(f"{BASE_URL}/products/{case['id']}", timeout=10)

    assert response.status_code == case["expected_status"]
    assert "id" in response.json()
