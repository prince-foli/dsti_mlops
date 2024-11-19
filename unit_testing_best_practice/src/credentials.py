"""Module for user credential input and validation."""

import re

def get_email() -> str:
    """
    Prompt the user to enter a valid email address.

    Returns:
        str: A valid email address containing '@' and '.'.
    """
    while True:
        print("Be sure to include an @ and a dot (.) in your email!")
        email = input("Enter your email: ")
        
        if '@' in email and '.' in email:
            return email
        print("Invalid email. Please try again.")


def get_username() -> str:
    """
    Prompt the user to enter a valid username.

    Returns:
        str: A valid username without spaces or tabulations.
    """
    while True:
        print("Your username is mandatory and must not contain spaces or tabulations!")
        username = input("Enter your username: ")
        
        if username and not re.search(r"\s", username):
            return username
        print("Invalid username. Please try again.")


def get_password() -> str:
    """
    Prompt the user to enter a valid password.

    The password must:
    - Be at least 8 characters long
    - Contain at least 1 number
    - Contain at least 1 letter
    - Contain at least 1 special character

    Returns:
        str: A valid password meeting the specified criteria.
    """
    special_characters = r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?~`]"
    
    while True:
        print("Your password must contain at least 8 characters, "
              "1 number, 1 letter, and 1 special character!")
        print(f"Authorized special characters are {special_characters}")
        password = input("Enter your password: ")
        
        if (len(password) >= 8 and 
            re.search(r"\d", password) and 
            re.search(r"[a-zA-Z]", password) and 
            re.search(special_characters, password)):
            return password
        print("Invalid password. Please try again.")


if __name__ == "__main__":
    valid_email = get_email()
    valid_username = get_username()
    valid_password = get_password()
    print(f"Your email: {valid_email}")
    print(f"Your username: {valid_username}")
    print(f"Your password: {valid_password}")