from requests import Response
from typing import Set, Any

def assert_status_code(response: Response, expected_status: int):
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"

def assert_json_has_keys(response: Response, keys: Set[str]):
    data = response.json()
    assert keys.issubset(data.keys()), "Response JSON Missing expected keys"

def assert_json_field_equals(response: Response, field: str, expected_value: Any):
    data: dict[str, Any] = response.json()
    assert data[field] == expected_value, f"Expected {field}={expected_value}, got {data.get(field)}"