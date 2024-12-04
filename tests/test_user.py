from fastapi.testclient import TestClient
from app.main import app

# Configuration of the test client
client = TestClient(app)

def test_create_user():
    # Create a user
    response = client.post(
        "/users/",
        json={"username": "username", "email": "testuser@example.com"},
    )
    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201
    data = response.json()
    # Assert that the name of the created user is correct
    assert data["name"] == "username"
    assert data["email"] == "testuser@example.com"

    # Clean up by deleting the user after the test
    response = client.delete(f"/users/{data['id']}")
    # Assert that the delete request was successful with a 200 status code
    assert response.status_code == 200

def test_get_user():
    # Get the list of user
    response = client.get("/users/")
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    # Assert that the list of users is not empty
    assert len(response.json()) > 0
