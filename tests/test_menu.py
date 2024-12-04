from fastapi.testclient import TestClient
from app.main import app

# Configuration of the test client
client = TestClient(app)

def test_create_menu():
    # Create a menu
    response = client.post(
        "/menus/",
        json={"name": "Temporary", "description": "Test menu."},
    )
    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201
    data = response.json()
    # Assert that the name of the created menu is correct
    assert data["name"] == "Temporary"

    # Clean up by deleting the menu after the test
    response = client.delete(f"/menu/{data['id']}")
    # Assert that the delete request was successful with a 200 status code
    assert response.status_code == 200

def test_get_menus():
    # Get the list of menus
    response = client.get("/menus/")
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    # Assert that the list of menus is not empty
    assert len(response.json()) > 0
