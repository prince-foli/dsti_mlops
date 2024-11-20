import re

def validate_username(username):
    if not username:
        return False  # Le nom d'utilisateur est vide
    if ' ' in username:
        return False  # Le nom d'utilisateur contient des espaces
    return True  # Le nom d'utilisateur est valide

def validate_password(password):
    if len(password) < 8:
        return False  # Moins de 8 caractères
    if not re.search(r"\d", password):
        return False  # Pas de chiffre
    if not re.search(r"[a-zA-Z]", password):
        return False  # Pas de lettre
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-]", password):  # Inclut - et _ dans les caractères spéciaux
        return False  # Pas de caractère spécial
    return True  # Mot de passe valide

def validate_email(email):
    if "@" not in email or "." not in email:
        return False  # Email invalide
    return True  # Email valide