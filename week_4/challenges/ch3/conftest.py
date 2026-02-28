from typing import Any
import pytest
import sqlite3
import os
import json


def load_json(file_path: str) -> dict[str, Any]:
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, file_path)
    with open(full_path) as file:
        return json.load(file)


@pytest.fixture(scope="session")
def db():
    data_filter = load_json("data/seeds.json")["list_of_products"]
    conn = sqlite3.connect("test.db")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            title TEXT,
            price REAL,         
            category TEXT
        ) 
    """
    )

    for item in data_filter:
        conn.execute(
            "INSERT INTO products(title, price, category) values (?, ?, ?)",
            (item["title"], item["price"], item["category"]),
        )
    conn.commit()

    yield conn

    conn.execute("DROP TABLE IF EXISTS products")
    conn.commit()
    conn.close()
