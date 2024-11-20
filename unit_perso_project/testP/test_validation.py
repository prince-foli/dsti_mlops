# test_validation.py
import pytest
import sys
import os

# Add the 'srcP' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'srcP')))

from validation import validate_username, validate_password, validate_email

# Test de la fonction de validation du nom d'utilisateur
def test_validate_username():
    assert validate_username("validUsername") == True
    assert validate_username("") == False
    assert validate_username("invalid username") == False

# Test de la fonction de validation du mot de passe
def test_validate_password():
    assert validate_password("Valid1!") == False
    assert validate_password("short") == False
    assert validate_password("NoSpecial123") == False
    assert validate_password("NoDigit!!") == False

# Test de la fonction de validation de l'email
def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid.com") == False
    assert validate_email("missingat.com") == False