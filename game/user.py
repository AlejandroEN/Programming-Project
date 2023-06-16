import json

def create_new_user(username: str, password: str):
    """Creates new instance of player request, stores player data as .JSON file."""

    new_player = {"username": username, "password": password}
    json_object = json.dumps(new_player, indent=4)

    with open(f"../data/{username}.json", "w") as storage:
        storage.write(json_object)

def check_user(username: str, password: str):
    """Performs rundown data carpet, if player information exists and is correct, allows access to code operations.
        Otherwise, prompts message and ends cycle."""

    try:
        with open(f"../data/{username}.json", "r") as storage:
            data = json.load(storage)
            return data["password"] == password
    except FileNotFoundError:
        return False