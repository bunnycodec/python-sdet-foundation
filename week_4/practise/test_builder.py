from typing import Any
import pytest


class UserBuilder:
    def __init__(self):
        self._user: dict[str, Any] = {
            "name": "Test User",
            "email": "test@example.com",
            "age": 25,
            "role": "customer",
            "active": True,
        }

    def with_name(self, name: str) -> "UserBuilder":
        self._user["name"] = name
        return self

    def with_email(self, email: str) -> "UserBuilder":
        self._user["email"] = email
        return self

    def with_age(self, age: int) -> "UserBuilder":
        self._user["age"] = age
        return self

    def with_role(self, role: str) -> "UserBuilder":
        self._user["role"] = role
        return self

    def with_active(self, active: bool) -> "UserBuilder":
        self._user["active"] = active
        return self

    def build(self):
        return self._user


@pytest.mark.now
def test_default_payload():
    user = UserBuilder().build()

    assert user["name"] == "Test User"
    assert user["email"] == "test@example.com"
    assert user["age"] == 25
    assert user["role"] == "customer"
    assert user["active"] == True


@pytest.mark.now
def test_admin_user():
    user = UserBuilder().with_role("admin").with_name("Admin User").build()

    assert user["role"] == "admin"
    assert user["name"] == "Admin User"


@pytest.mark.now
def test_inactive_underage_user():
    user = UserBuilder().with_age(16).with_active(False).build()

    assert user["age"] == 16
    assert user["active"] == False
