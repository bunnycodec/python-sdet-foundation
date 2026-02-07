import requests
from typing import Any
from config.config import BASE_URL

def get(endpoint: str, params: dict[str, str|int] | None = None):
    return requests.get(BASE_URL + endpoint, params=params)

def post(endpoint: str, payload: dict[str, Any] | None = None):
    return requests.post(BASE_URL + endpoint, json=payload)

