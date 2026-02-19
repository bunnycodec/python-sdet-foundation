import requests
import uuid


def test_complete_user_lifecycle(api_client: requests.Session, base_url: str):
    unique_email = f"bunny_{uuid.uuid4().hex[:8]}@email.com"
    payload = {
        "name": "Bunny",
        "email": unique_email,
        "gender": "male",
        "status": "inactive",
    }

    # Step 1: Create user with inactive status
    response = api_client.post(f"{base_url}/users", json=payload, timeout=10)
    user_id = response.json()["id"]
    assert response.status_code == 201, "User was not created!"

    # Step 2: Verify user creation
    response = api_client.get(f"{base_url}/users/{user_id}", timeout=10)
    assert response.status_code == 200, "Invalid User!"

    # Step 3: Activate user
    patch_payload = {"status": "active"}
    response = api_client.patch(
        f"{base_url}/users/{user_id}", json=patch_payload, timeout=10
    )
    assert response.status_code == 200, "Status Not Updated!"

    # Step 4: Verify activation persisted
    response = api_client.get(f"{base_url}/users/{user_id}", timeout=10)
    data = response.json()
    assert data["status"] == "active", "Status Not Updated!"

    # Step 5: Update user name
    patch_payload = {"name": "Bunny Updated"}
    response = api_client.patch(
        f"{base_url}/users/{user_id}", json=patch_payload, timeout=10
    )
    assert response.status_code == 200, "Name Not Updated!"

    # Step 6: Verify name update and status unchanged
    response = api_client.get(f"{base_url}/users/{user_id}", timeout=10)
    data = response.json()
    assert data["name"] == "Bunny Updated", "Name Not Updated!"
    assert data["status"] == "active", "Status got changed without changing!"

    # Step 7: Deactivate user
    patch_payload = {"status": "inactive"}
    response = api_client.patch(
        f"{base_url}/users/{user_id}", json=patch_payload, timeout=10
    )
    assert response.status_code == 200, "Status Not Updated!"

    # Step 8: Verify deactivation and name unchanged
    response = api_client.get(f"{base_url}/users/{user_id}", timeout=10)
    data = response.json()
    assert data["status"] == "inactive", "Status was not updated!"
    assert data["name"] == "Bunny Updated", "Name got changed without changing!"

    # Step 9: Delete user
    response = api_client.delete(f"{base_url}/users/{user_id}", timeout=10)
    assert response.status_code == 204, "User was not deleted!"

    # Step 10: Verify deletion
    response = api_client.get(f"{base_url}/users/{user_id}", timeout=10)
    assert response.status_code == 404, "User still exist!"
