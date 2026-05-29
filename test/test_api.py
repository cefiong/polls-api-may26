import pytest
import requests
import time
from test.conftest import BASE_URL

def test_health_check():
    response = requests.get(f"{BASE_URL}/health")

    # Assert: check status code
    assert response.status_code == 200

    # Assert: check if status is healthy
    data = response.json()

    assert data["status"] == "healthy"

def test_register_user():
    # Arrange: Create a random user
    current_time = int(time.time() * 1000)

    new_user = {
        "username": f"user123_{current_time}",
        "password": "pass123"
        
    }
    # Act: Register the user
    response = requests.post(f"{BASE_URL}/auth/register", json=new_user)

    # Assert: Check for valid status code
    assert response.status_code == 201

    data = response.json()

    # Assert: Check if user is admin
    assert data["user"]["is_admin"] == True

    # Assert:  
    assert data["user"]["username"] == new_user["username"]

    # Assert:Check if username is correct
    assert data["user"]["username"] != "myawesomeuser" 


def test_register_user2():
    # Arrange: Create a random user
    current_time = int(time.time() * 1000)

    new_user = {
        "username": f"user123_{current_time}",
        "password": "pass123"
        
    }
    # Act: Register the user
    response = requests.post(f"{BASE_URL}/auth/register", json=new_user)

    # Assert: Check for valid status code
    assert response.status_code == 201

    data = response.json()

    # Assert: Check if user is admin
    assert data["user"]["is_admin"] == False

    # Assert:  
    assert data["user"]["username"] == new_user["username"]

    # Assert:Check if username is correct
    assert data["user"]["username"] != "myawesomeuser" 



def test_create_polls(auth_token):
    # Arrange
    new_poll = {
        "question": "What is your favorite framework?",
        "options": [
            "React",
            "Vue",
            "Angular",
            "Django",
            "FastAPI",
            "Flask",
        
        ],
        "is_public": False,
        "requires_admin": False
    }

    # Act
    headers = {"Authorization": f"Bearer {auth_token}" }
    response = requests.post(f"{BASE_URL}/polls", json=new_poll, headers=headers)

    # Assert: check status code
    assert response.status_code == 201

    poll_data = response.json()

    # Act vote on a poll
    new_vote = {
        "choice": "Vue"
    }
    poll_id = poll_data["id"]

    response = requests.post(f"{BASE_URL}/votes/poll/{poll_id}", json=new_vote, headers=headers)

    assert response.status_code == 201


