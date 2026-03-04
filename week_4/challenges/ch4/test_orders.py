import builders
import pytest
from typing import Any


@pytest.mark.smoke
def test_default_order_payload():
    payload = builders.OrderBuilder().build()

    assert payload["customer"]["name"] == "Test Customer"
    assert payload["customer"]["email"] == "test@customer.com"
    assert payload["customer"]["address"] == "123 Test Street"
    assert payload["customer"]["country"] == "UK"
    assert payload["products"] == []
    assert payload["status"] == "pending"
    assert payload["total"] == 0.0


@pytest.mark.smoke
def test_custom_order_payload():
    customer = builders.CustomerBuilder().with_name("John Doe").build()
    product_1: dict[str, Any] = {"id": 1, "title": "Product 1", "price": 10.0}
    product_2: dict[str, Any] = {"id": 2, "title": "Product 2", "price": 20.0}

    payload = (
        builders.OrderBuilder()
        .with_customer(customer)
        .with_product(product_1)
        .with_product(product_2)
        .with_status("confirmed")
        .with_total(30.0)
        .build()
    )

    assert payload["customer"]["name"] == "John Doe"
    assert payload["products"] == [product_1, product_2]
    assert payload["status"] == "confirmed"
    assert payload["total"] == 30.0


@pytest.mark.smoke
def test_order_with_multiple_products():
    product_1: dict[str, Any] = {"id": 1, "title": "Product 1", "price": 10.0}
    product_2: dict[str, Any] = {"id": 2, "title": "Product 2", "price": 20.0}
    product_3: dict[str, Any] = {"id": 3, "title": "Product 3", "price": 30.0}

    payload = (
        builders.OrderBuilder()
        .with_product(product_1)
        .with_product(product_2)
        .with_product(product_3)
        .build()
    )

    assert payload["products"] == [product_1, product_2, product_3]


@pytest.mark.smoke
def test_order_with_shipped_status_and_high_total():
    payload = builders.OrderBuilder().with_status("shipped").with_total(150.0).build()

    assert payload["status"] == "shipped"
    assert payload["total"] > 100


@pytest.mark.smoke
def test_empty_order_with_cancelled_status():
    payload = (
        builders.OrderBuilder()
        .with_customer({"name": "", "email": "", "address": "", "country": ""})
        .with_status("cancelled")
        .build()
    )

    assert payload["customer"]["name"] == ""
    assert payload["products"] == []
    assert payload["status"] == "cancelled"
    assert payload["total"] == 0.0
