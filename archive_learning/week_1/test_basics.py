from typing import Any

def is_adult(age: int) -> str:
    if age >= 18:
        return "Adult"
    else:
        return "Not Adult"

def test_multiplication():
    assert 5*8 == 40

def test_string_operation():
    assert " my-Name-Is-Bunny  ".strip().lower().split("-")[-1] == "bunny"

def test_list_behaviour():
    assert "mango" in ["car", "mango", "apple", "wheel"]

def test_dict_access():
    user_data: dict[str, Any] = {"id": 101, "role": "admin", "active": True}
    assert "role" in user_data

def test_function_return_values():
    assert is_adult(23) == "Adult"