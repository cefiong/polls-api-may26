import pytest
from models import User

def test_user_password_hash():
    user = User(username="test123")
    user.set_password("pass123")

    assert user.check_password("pass123") == True

    assert user.password_hash != "pass123"

