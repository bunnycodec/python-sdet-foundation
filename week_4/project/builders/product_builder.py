from typing import Any


class ProductBuilder:
    def __init__(self):
        self._product: dict[str, Any] = {
            "title": "Dummy Product",
            "description": "This is a dummy product for testing purposes.",
            "price": 9.99,
            "category": "dummy-category",
        }

    def with_title(self, title: str) -> "ProductBuilder":
        self._product["title"] = title
        return self

    def with_description(self, description: str) -> "ProductBuilder":
        self._product["description"] = description
        return self

    def with_price(self, price: float) -> "ProductBuilder":
        self._product["price"] = price
        return self

    def with_category(self, category: str) -> "ProductBuilder":
        self._product["category"] = category
        return self

    def build(self) -> dict[str, Any]:
        return self._product
