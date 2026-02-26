import requests
import pytest
import csv

BASE_URL = "https://fakestoreapi.com/products"


@pytest.mark.smoke
@pytest.mark.parametrize("product_id, expected", [(999, 404)])
def test_get_product_by_id(product_id: int, expected: int):
    response = requests.get(f"{BASE_URL}/{product_id}", timeout=10)

    assert response.status_code == expected
    if expected == 200:
        prod_data = response.json()
        assert prod_data["id"] == product_id


def load_csv(filepath: str):
    with open(filepath, newline="") as file:
        reader = csv.DictReader(file)
        return [
            (int(row["limit"]), int(row["expected_status"]), int(row["expected_count"]))
            for row in reader
        ]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "limit, expected_status, expected_count", load_csv("products.csv")
)
def test_filter_products_by_limit(
    limit: int, expected_status: int, expected_count: int
):
    response = requests.get(f"{BASE_URL}?limit={limit}", timeout=10)
    prod_data = response.json()

    assert response.status_code == expected_status
    assert len(prod_data) == expected_count
