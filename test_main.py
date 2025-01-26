import pytest
from main import generate_password

def test_generate_password():
    password = generate_password(10, True)
    assert len(password) == 10
    assert any(char in "!@#$%^&*()_+" for char in password)