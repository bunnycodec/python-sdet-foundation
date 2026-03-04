import json
from typing import Any


def load_json(filepath: str) -> Any:
    with open(filepath) as file:
        return json.load(file)
