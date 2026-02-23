import requests
import pytest
import schemas
from faker import Faker
from jsonschema import validate
from typing import Any


@pytest.mark.smoke
def test_create_post_201(
    created_user: dict[str, Any], api_client: requests.Session, base_url: str
):
    fake = Faker()
    payload: dict[str, Any] = {
        "user_id": created_user["id"],
        "title": fake.sentence(nb_words=3),
        "body": fake.paragraph(nb_sentences=3),
    }
    response = api_client.post(f"{base_url}/posts", json=payload, timeout=10)
    post_id = response.json()["id"]
    assert response.status_code == 201, f"Failed to create Post: {response.text}"

    api_client.delete(f"{base_url}/posts/{post_id}", timeout=10)


@pytest.mark.smoke
def test_read_post_200(
    created_post: dict[str, Any], api_client: requests.Session, base_url: str
):
    post_id = created_post["id"]
    response = api_client.get(f"{base_url}/posts/{post_id}", timeout=10)
    post_data = response.json()

    assert response.status_code == 200, f"Failed to Get Post: {response.text}"
    assert post_data["title"] == created_post["title"]


@pytest.mark.smoke
def test_update_post_title_200(
    created_post: dict[str, Any], api_client: requests.Session, base_url: str
):
    post_id = created_post["id"]
    payload = {"title": "Updated Post"}
    response = api_client.patch(f"{base_url}/posts/{post_id}", json=payload, timeout=10)
    post_data = response.json()

    assert response.status_code == 200, f"Failed to Update Post: {response.text}"
    assert post_data["title"] == payload["title"]

    response = api_client.get(f"{base_url}/posts/{post_id}", timeout=10)
    assert response.json()["title"] == payload["title"]


@pytest.mark.smoke
def test_update_post_body_200(
    created_post: dict[str, Any], api_client: requests.Session, base_url: str
):
    post_id = created_post["id"]
    payload = {"body": "Updated Post Body"}
    response = api_client.patch(f"{base_url}/posts/{post_id}", json=payload, timeout=10)
    post_data = response.json()

    assert response.status_code == 200, f"Failed to Update Post Body: {response.text}"
    assert post_data["body"] == payload["body"]

    response = api_client.get(f"{base_url}/posts/{post_id}", timeout=10)
    assert response.json()["body"] == payload["body"]


@pytest.mark.smoke
def test_delete_post_204(
    created_user: dict[str, Any], api_client: requests.Session, base_url: str
):
    fake = Faker()
    payload: dict[str, Any] = {
        "user_id": created_user["id"],
        "title": fake.sentence(nb_words=3),
        "body": fake.paragraph(nb_sentences=3),
    }
    response = api_client.post(f"{base_url}/posts", json=payload, timeout=10)
    assert response.status_code == 201, f"Failed to create Post: {response.text}"

    post_id = response.json()["id"]
    response = api_client.delete(f"{base_url}/posts/{post_id}", timeout=10)
    assert response.status_code == 204

    response = api_client.get(f"{base_url}/posts/{post_id}", timeout=10)
    assert response.status_code == 404


@pytest.mark.smoke
def test_post_schema(
    created_post: dict[str, Any], api_client: requests.Session, base_url: str
):
    post_id = created_post["id"]
    response = api_client.get(f"{base_url}/posts/{post_id}", timeout=10)
    post_data = response.json()

    validate(instance=post_data, schema=schemas.post_schema)


@pytest.mark.smoke
def test_post_list_schema(api_client: requests.Session, base_url: str):
    response = api_client.get(f"{base_url}/posts", timeout=10)
    post_data = response.json()

    validate(instance=post_data, schema=schemas.posts_list_schema)


@pytest.mark.smoke
def test_create_post_schema(
    created_user: dict[str, Any], api_client: requests.Session, base_url: str
):
    fake = Faker()
    payload: dict[str, Any] = {
        "user_id": created_user["id"],
        "title": fake.sentence(nb_words=3),
        "body": fake.paragraph(nb_sentences=3),
    }
    response = api_client.post(f"{base_url}/posts", json=payload, timeout=10)
    post_data = response.json()
    assert response.status_code == 201, f"Failed to create Post: {response.text}"

    validate(instance=post_data, schema=schemas.post_schema)
    post_id = post_data["id"]
    api_client.delete(f"{base_url}/posts/{post_id}", timeout=10)


@pytest.mark.smoke
def test_posts_specific_user_validate_200(
    created_user: dict[str, Any], api_client: requests.Session, base_url: str
):
    user_id = created_user["id"]
    response = api_client.get(f"{base_url}/users/{user_id}/posts", timeout=10)
    post_data = response.json()

    assert response.status_code == 200
    assert all(post["user_id"] == user_id for post in post_data)


@pytest.mark.smoke
def test_create_post_specific_user_200(
    created_user: dict[str, Any], api_client: requests.Session, base_url: str
):
    user_id = created_user["id"]
    fake = Faker()
    payload: dict[str, Any] = {
        "user_id": user_id,
        "title": fake.sentence(nb_words=3),
        "body": fake.paragraph(nb_sentences=3),
    }
    response = api_client.post(
        f"{base_url}/users/{user_id}/posts", json=payload, timeout=10
    )
    post_data = response.json()

    assert response.status_code == 201, f"Failed to create Post: {response.text}"
    assert post_data["title"] == payload["title"]

    api_client.delete(f"{base_url}/posts/{post_data['id']}", timeout=10)


@pytest.mark.smoke
def test_missing_title_422(
    created_user: dict[str, Any], api_client: requests.Session, base_url: str
):
    fake = Faker()
    payload: dict[str, Any] = {
        "user_id": created_user["id"],
        "body": fake.paragraph(nb_sentences=3),
    }
    response = api_client.post(f"{base_url}/posts", json=payload, timeout=10)
    error_data = response.json()

    assert response.status_code == 422
    assert any("title" in str(err).lower() for err in error_data)


@pytest.mark.smoke
def test_invalid_user_422(
    created_user: dict[str, Any], api_client: requests.Session, base_url: str
):
    fake = Faker()
    payload: dict[str, Any] = {
        "user_id": 999999999,
        "title": fake.sentence(nb_words=3),
        "body": fake.paragraph(nb_sentences=3),
    }
    response = api_client.post(f"{base_url}/posts", json=payload, timeout=10)
    error_data = response.json()

    assert response.status_code == 422
    assert any("must exist" in str(err).lower() for err in error_data)
