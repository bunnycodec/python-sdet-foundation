import json
import os
import requests
import pytest

BASE_URL = "https://fakestoreapi.com"


def load_json(filepath: str):
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, filepath)
    with open(full_path) as file:
        return json.load(file)


@pytest.mark.smoke
@pytest.mark.parametrize("case", load_json("data/perf.json")["get_all_products"])
def test_get_all_products(case: dict[str, int]):
    response = requests.get(f"{BASE_URL}/products", timeout=10)

    assert response.status_code == case["expected_status"]
    assert response.elapsed.total_seconds() * 1000 < case["max_response_time_ms"]


@pytest.mark.smoke
@pytest.mark.parametrize("case", load_json("data/perf.json")["get_product_by_id"])
def test_get_product_by_id(case: dict[str, int]):
    response = requests.get(f"{BASE_URL}/products/{case['id']}", timeout=10)

    assert response.status_code == case["expected_status"]
    assert response.elapsed.total_seconds() * 1000 < case["max_response_time_ms"]


@pytest.mark.smoke
@pytest.mark.parametrize("case", load_json("data/perf.json")["create_product"])
def test_create_product(case: dict[str, int]):
    payload = case["payload"]
    response = requests.post(f"{BASE_URL}/products", json=payload, timeout=10)

    assert response.status_code == case["expected_status"]
    assert response.elapsed.total_seconds() * 1000 < case["max_response_time_ms"]
