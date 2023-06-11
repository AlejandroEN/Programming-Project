import json
def create_new_user(username: str, password: str):
    new_player = {"username": username, "password": password}
    json_object = json.dumps(new_player, indent=4)

    with open(f"Data/{username}.json", "w") as storage:
        storage.write(json_object)

def check_user(username: str, password: str):
    try:
        with open(f"Data/{username}.json", "r") as storage:
            data = json.load(storage)
            return data["password"] == password
    except FileNotFoundError:
        return False