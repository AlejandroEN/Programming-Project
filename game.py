import json
from rich.prompt import Prompt
import board

class GameApp:
    def __init__(self):
        self.show_first_menu()

    def show_welcome(self):
        return 0

    def show_first_menu(self):
        first_menu_items = ["1. Registrar jugador",
                            "2. Establecer nuevo jugador",
                            "3. Iniciar juego de memoria",
                            "4. Salir"]

        choice = Prompt.ask("Seleccione una de las siguientes opciones:", choices=first_menu_items)


    def write_to_json(self, username: str, password: str):
        new_player = {"username": username, "password": password}
        json_object = json.dumps(new_player, indent=4)

        with open(f"Data/{username}.json", "w") as storage:
            storage.write(json_object)


new_game = GameApp()

