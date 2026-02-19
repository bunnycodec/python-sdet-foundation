from typing import Any


user_schema: dict[str, Any] = {
    "type": "object",
    "required": ["id", "name", "email", "gender", "status"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "gender": {"type": "string"},
        "status": {"type": "string"},
    },
}

user_list_schema: dict[str, Any] = {"type": "array", "items": user_schema}
