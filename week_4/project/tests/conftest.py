import sqlite3
import pytest
import os
from utils.file_loader import load_json


@pytest.fixture(scope="session")
def db():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_filter = load_json(os.path.join(base_dir, "data/products.json"))[
        "list_of_products"
    ]

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
