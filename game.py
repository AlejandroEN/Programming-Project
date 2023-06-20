from packages import user
from models.board_model import Board
from packages.simple_list_selection import ask
from getpass import getpass
from random import randint
from packages.card import get_pairs_of_cards

board: Board = Board()

def run() -> None:
    show_welcome()

def show_welcome() -> None:
    welcome: str = "This is a welcome"
    print(f"{welcome}\n")

def show_first_menu() -> None:
    menu_items: list[str] = ["Registrar jugador", "Establecer turno", "Iniciar juego de memoria", "Salir"]
    choice:int = ask("Seleccione una de las siguientes opciones:", menu_items)

    match choice:
        case 0: create_new_user()
        case 1: set_difficulty()
        case 2: run_memory_game()
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
    number_of_players = 0

    while number_of_players > 4 or number_of_players < 2:
        number_of_players = int(input("Ingreses la cantidad de jugadores (2 a 4): "))

    print()
    verified_players = []

    for i in range(number_of_players):
        while True:
            print(f"Jugador {i + 1}:")
            username = input("Ingrese su usuario: ")
            password = getpass("Ingrese su contraseña: ")

            if check_user(username, password):
                verified_players.append(username)
                break
            else:
                print("Usuario o contraseña incorrectos. Intente de nuevo, por favor.\n")

    players_card_dictionary, playing_order = get_players_order(verified_players)

    for i in players_card_dictionary:
        card: tuple[str, list[str]] = get_reformatted_card(players_card_dictionary[i])
        print(f"Carta para «{i}»: {card[0]}{card[1][(randint(0, 1))]}")

    print()

    # Falta contemplar el caso en que las cartas retornadas sean iguales

    for i in range(len(playing_order)):
        print(f"Turno {i + 1}: {playing_order[i][0]}")


def run_memory_game() -> None:
    # if not players_order:
    #     print("No se ha establecido el orden de los jugadores.")
    #     print("Por favor, seleccione la opción 2 y establezca el orden de los jugadores antes de iniciar el juego.\n")
    #     show_first_menu()
    #
    # print("Juego de memoria iniciado.\n")
    # print("¡Buena suerte!\n")
    # display_board(is_numbered=True)

    get_players_order(["Jugador 1", "Jugador 2", "Jugador 3", "Jugador 4"])
    turn = 0

    while True:
        print(f"Turno de jugador «{players_order[turn][0]}»")
        turn += 1
        turn %= len(players_order)
        card_1_position = int(input("Ingrese la posición de la primera carta: "))
        card_2_position = int(input("Ingrese la posición de la segunda carta: "))


set_difficulty(1)
run_memory_game()