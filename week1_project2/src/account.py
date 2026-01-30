from typing import Any

class Account:
    def __init__(self, account_number: int, name: str, age: int) -> None:
        self.account_number = account_number
        self.name = name
        self.age = age
        self.balance = 0.0
        self.transactions: list[dict[str, Any]] = []
