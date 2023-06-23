from packages import user
from simple_list_selection import ask
from getpass import getpass
from card import get_pairs_of_cards, get_players_order
from board_model import Board
from player_model import Player

board: Board = Board()
players: list[Player] = []

def run() -> None:
    welcome: str = "This is a welcome"
    print(f"{welcome}\n")
    show_first_menu()

def show_first_menu() -> None:
    menu_items: list[str] = ["Registrar jugador", "Establecer dificultad y turnos", "Iniciar juego de memoria", "Salir"]
    choice: int = ask("Seleccione una de las siguientes opciones:", menu_items)

    match choice:
        case 0: create_new_user()
        case 1: set_difficulty()
        case 2: start()
        case 4: exit()

def create_new_user() -> None:
    username: str = input("Usuario: ")
    password: str = getpass("Contraseña: ")
    user.create_new_user(username, password)
    show_first_menu()

def set_difficulty() -> None:
    menu_items: list[str] = ["Fácil", "Normal", "Difícil"]
    board.difficulty = ask("Seleccione la dificultad:", menu_items)
    pairs_of_cards: int = 0

    match board.difficulty:
        case 0: pairs_of_cards = 8
        case 1: pairs_of_cards = 16
        case 2: pairs_of_cards = 26

    board.fill(get_pairs_of_cards(pairs_of_cards))
    set_players_order()

def set_players_order() -> None:
    global players

    number_of_players: int = 0
    while number_of_players > 4 or number_of_players < 2: number_of_players = int(input("Ingreses la cantidad de jugadores (2 a 4): "))
    print()
    verified_players: list[Player] = []

    for i in range(number_of_players):
        while True:
            print(f"Jugador {i + 1}:")
            username: str = input("Ingrese su usuario: ")
            password: str = getpass("Ingrese su contraseña: ")

            if user.check_user(username, password):
                verified_players.append(Player(username))
                break
            else:
                print("Usuario o contraseña incorrectos. Intente de nuevo, por favor.\n")

    card_per_player, players = get_players_order(verified_players)

    for player in card_per_player:
        card = card_per_player[player]
        print(f"Carta para «{player.username}»: {card.value}{card.suit}")

    print()

    for i in range(len(players)): print(f"Turno {i + 1}: {players[i].username}")  # Todo: Falta contemplar el caso en que las cartas retornadas sean iguales
    print()

    show_first_menu()

def start() -> None:
    if not players:
        print("No se ha establecido el orden de los jugadores.")
        print("Por favor, seleccione la opción 2 y establezca el orden de los jugadores antes de iniciar el juego.\n")
        show_first_menu()

    print("Juego de memoria iniciado.\n")
    print("¡Buena suerte!\n")
    player_index_turn: int = 0

    while sum([player.score for player in players]) < len(board.cards) / 2:
        player = players[player_index_turn]
        board.display()
        print(f"\nTurno de «{player.username}»:")
        card_1_position: int = int(input("Ingrese la posición de la primera carta: "))
        card_2_position: int = int(input("Ingrese la posición de la segunda carta: "))
        # ToDo: Check card's values before comparing them (must be between 0 and len(board.cards) - 1)
        # ToDo: if Card position is invalid, ask for a new one.
        # ToDo: If user enters the same position for both cards, ask again for the second card's position
        print()
        board.cards[card_1_position].is_visible = board.cards[card_2_position].is_visible = True
        board.display()
        print([f"{player.username}: {player.score} | " for player in players])

        if board.cards[card_1_position] == board.cards[card_2_position]:
            player.score += 1
            print("¡Cartas iguales! Ganaste un punto y tienes un turno adicional.\n")
        else:
            print("¡Cartas diferentes! No ganaste ningún punto y tu turno ha finalizado.\n")
            player_index_turn += 1 if player_index_turn < len(players) - 1 else 0


if __name__ == "__main__":
    run()