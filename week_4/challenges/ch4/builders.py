from typing import Any


class CustomerBuilder:
    def __init__(self):
        self._user: dict[str, Any] = {
            "name": "Test Customer",
            "email": "test@customer.com",
            "address": "123 Test Street",
            "country": "UK",
        }

    def with_name(self, name: str) -> "CustomerBuilder":
        self._user["name"] = name
        return self

    def with_email(self, email: str) -> "CustomerBuilder":
        self._user["email"] = email
        return self

    def with_address(self, address: str) -> "CustomerBuilder":
        self._user["address"] = address
        return self

    def with_country(self, country: str) -> "CustomerBuilder":
        self._user["country"] = country
        return self

    def build(self):
        return self._user


class OrderBuilder:
    def __init__(self):
        self._order: dict[str, Any] = {
            "customer": CustomerBuilder().build(),
            "products": [],
            "status": "pending",
            "total": 0.0,
        }

    def with_customer(self, customer: dict[str, Any]) -> "OrderBuilder":
        self._order["customer"] = customer
        return self

    def with_product(self, product: dict[str, Any]) -> "OrderBuilder":
        self._order["products"].append(product)
        return self

    def with_status(self, status: str) -> "OrderBuilder":
        self._order["status"] = status
        return self

    def with_total(self, total: float) -> "OrderBuilder":
        self._order["total"] = total
        return self

    def build(self) -> dict[str, Any]:
        return self._order
