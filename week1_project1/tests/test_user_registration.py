import pytest
from src.user_registration import UserService


def test_register_user_success():
    service = UserService()

    user = service.register_user("Bunny", "bunny@test.com", 21)
    assert user.name == "Bunny"
    assert user.email == "bunny@test.com"
    assert user.age == 21

def test_register_user_underage():
    service = UserService()

    with pytest.raises(ValueError, match="cannot be less than 18 years old."):
        service.register_user("Bunny", "bunny@test.com", 15)

def test_register_user_invalid_email_format():
    service = UserService()

    with pytest.raises(ValueError, match="must contain exactly one @"):
        service.register_user("Bunny", "bunny@@test.com", 23)

    with pytest.raises(ValueError, match="domain must contain a dot"):
        service.register_user("Bunny", "bunny@testcom", 23)

def test_register_user_invalid_name():
    service = UserService()

    with pytest.raises(ValueError, match="cannot be empty or whitespace"):
        service.register_user("  ", "bunny@test.com", 23)