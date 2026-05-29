import pytest
import requests
import time


BASE_URL = "http://localhost:5001/api"

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def auth_token():

    # Create a random user
    current_time = int(time.time() * 1000)

    new_user = {
        "username": f"user123_{current_time}",
        "password": "pass123"
        
    }

    # Register the user
    response = requests.post(f"{BASE_URL}/auth/register", json=new_user)


    # Login the user
    response = requests.post(f"{BASE_URL}/auth/login", json=new_user)
    token = response.json()["access_token"]

    # return the token
    return token
