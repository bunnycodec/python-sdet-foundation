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

post_schema: dict[str, Any] = {
    "type": "object",
    "required": ["id", "user_id", "title", "body"],
    "properties": {
        "id": {"type": "integer"},
        "user_id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
}

users_list_schema: dict[str, Any] = {"type": "array", "items": user_schema}

posts_list_schema: dict[str, Any] = {"type": "array", "items": post_schema}
