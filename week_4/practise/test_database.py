import pytest
import sqlite3


@pytest.fixture
def db():
    conn = sqlite3.connect("test.db")

    yield conn

    conn.execute("DELETE FROM products")
    conn.commit()
    conn.close()


@pytest.mark.smoke
def test_create_insert_validate(db: sqlite3.Connection):
    cursor = db.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL           
        )
        """
    )
    db.commit()

    cursor.execute("INSERT INTO products(name, price) VALUES (?, ?)", ("Naruto", 20.7))
    cursor.execute("INSERT INTO products(name, price) VALUES (?, ?)", ("Itachi", 25.7))
    cursor.execute("INSERT INTO products(name, price) VALUES (?, ?)", ("Jiraya", 28.7))
    db.commit()

    cursor.execute("SELECT COUNT(*) from products")
    result = cursor.fetchone()
    assert result[0] == 3

    cursor.execute("SELECT name from products WHERE name = ?", ("Itachi",))
    result = cursor.fetchone()
    assert result[0] == "Itachi"
