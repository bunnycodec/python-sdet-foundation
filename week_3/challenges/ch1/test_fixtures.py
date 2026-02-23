import requests


def test_get_users(api_client: requests.Session, base_url: str):
    response = api_client.get(f"{base_url}/users", timeout=10)
    assert response.status_code == 200
