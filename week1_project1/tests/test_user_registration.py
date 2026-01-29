import pytest
from src.user_registration import UserService, User

@pytest.fixture
def service():
    return UserService()

def test_register_user_success(service: UserService):
    user = service.register_user("Bunny", "bunny@example.com", 25)
    
    assert isinstance(user, User)
    assert user.name == "Bunny"
    assert user.email == "bunny@example.com"
    assert user.age == 25

def test_register_user_underage(service: UserService):
    with pytest.raises(ValueError, match="cannot be less than 18 years old."):
        service.register_user("Young User", "test@test.com", 17)

def test_register_user_invalid_email_format(service: UserService):
    with pytest.raises(ValueError, match="Email ID is not valid."):
        service.register_user("John", "john@com", 30)
    
    with pytest.raises(ValueError, match="Email ID is not valid."):
        service.register_user("John", "john@@example.com", 30)

def test_register_user_empty_name(service: UserService):
    with pytest.raises(ValueError, match="cannot be empty or whitespace."):
        service.register_user("   ", "john@example.com", 30)