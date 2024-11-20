"""Unit tests for credential validation functions."""

import os
import re
import sys
import pytest

# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Now you can import from credentials
from credentials import *

@pytest.fixture
def valid_email():
    """Provide a valid email for testing."""
    return "mydsti@account.com"

@pytest.fixture
def valid_username():
    """Provide a valid username for testing."""
    return "mydsti"

@pytest.fixture
def valid_password():
    """Provide a valid password for testing."""
    return r'Qe:"5Z[]-H5$g^,=[^='

@pytest.fixture
def special_characters():
    """Provide a set of special characters for password validation."""
    return r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?~`]"

def test_get_a_dot_in_email(valid_email):
    """Test if the email contains a dot."""
    assert '.' in valid_email, "Email must contain a dot (.) symbol"

def test_get_a_symbol_in_email(valid_email):
    """Test if the email contains an @ symbol."""
    assert '@' in valid_email, "Email must contain an @ symbol"

def test_get_an_username_not_empty(valid_username):
    """Test if the username is not empty."""
    assert valid_username, "Username must not be empty"

def test_get_an_username_without_space(valid_username):
    """Test if the username doesn't contain spaces or tabs."""
    assert not re.search(r"\s", valid_username), "Username must not contain space or tabulation"

def test_get_a_password_at_least_eight_characters_long(valid_password):
    """Test if the password is at least 8 characters long."""
    assert len(valid_password) >= 8, "Password must be at least 8 characters long"

def test_get_a_password_with_at_least_a_number(valid_password):
    """Test if the password contains at least one number."""
    assert re.search(r"\d", valid_password), "Password must contain at least 1 number"

def test_get_a_password_with_at_least_a_letter(valid_password):
    """Test if the password contains at least one letter."""
    assert re.search(r"[a-zA-Z]", valid_password), "Password must contain at least 1 letter"

def test_get_a_password_with_at_least_a_special_character(valid_password, special_characters):
    """Test if the password contains at least one special character."""
    assert re.search(special_characters, valid_password), "Password must contain at least 1 special character"