import json
from os.path import exists
from string import ascii_letters
from config import program_path

def create_new_user(username: str, password: str) -> str:
    """
    Creates new instance of player request, stores player data as .JSON file.
    """
    new_player: dict[str, str] = {"username": username, "password": _encrypt_password(password)}
    json_object: str = json.dumps(new_player, indent=4)

    if exists(f"{program_path}/data/{username}.json"):
        return "\nEl usuario ingresado ya existe.\n"
    else:
        with open(f"{program_path}/data/{username}.json", "w") as storage: storage.write(json_object)
        return "\nUsuario creado exitosamente.\n"

def check_user(username: str, password: str) -> bool:
    """
    Performs rundown data carpet, if player information exists and is correct, allows access to code operations.
    Otherwise, prompts message and ends cycle.
    """
    try:
        with open(f"{program_path}/data/{username}.json", "r") as storage:
            data = json.load(storage)
            return _decrypt_password(data["password"]) == password
    except FileNotFoundError:
        return False

def _encrypt_password(unencrypted_password: str) -> str:
    """
    Function encrypts selected string for password using the "Peanut Butter" method.
    Returns encrypted password string.
    """
    reversed_password: str = unencrypted_password[::-1]
    vocabulary: str = ascii_letters

    # Cambia cada letra para la izquierda en el vocabulario
    encrypted_password: str = ""

    for char in reversed_password:
        if char.isalpha():
            # Find the new position of the character in the vocabulary
            index: int = (vocabulary.index(char) - 1) % len(vocabulary)
            encrypted_password += vocabulary[index]
        else:
            encrypted_password += char

    return encrypted_password

def _decrypt_password(encrypted_password: str) -> str:
    """
    Function decrypts selected string for password using the "Peanut Butter" method.
    Returns decrypted password string.
    """
    reversed_password: str = encrypted_password[::-1]
    vocabulary: str = ascii_letters

    decrypted_password: str = ""

    for char in reversed_password:
        if char.isalpha():
            index: int = (vocabulary.index(char) + 1) % len(vocabulary)
            decrypted_password += vocabulary[index]
        else:
            decrypted_password += char

    return decrypted_password