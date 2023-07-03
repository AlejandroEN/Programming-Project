from packages import user
from packages.simple_list_selection import ask
from getpass import getpass
from packages.card import get_pairs_of_cards, get_players_order
from packages.models.board_model import Board
from packages.models.player_model import Player
from random import shuffle

def run() -> None:
    """
    Runs the game.
    """
    with open("res/welcome.txt") as file: welcome: str = file.read()
    print(f"\n{welcome}\n")
    show_menu([], Board())

def show_menu(players: list[Player], board: Board) -> None:
    """
    Shows the main menu.
    """
    menu_items: list[str] = ["Registrar jugador",
                             "Establecer dificultad y turnos",
                             "Iniciar juego de memoria",
                             "Guardar jugadores",
                             "Salir"]

    choice: int = ask("Seleccione una de las siguientes opciones:", menu_items)

    match choice:
        case 0:
            create_new_user()
            show_menu(players, board)
        case 1:
            show_menu(set_players_order(), set_difficulty())
        case 2:
            start(players, board)
        case 4:
            exit()
        case _:
            pass

def create_new_user() -> None:
    """
    Creates a new user.
    """
    username: str = input("Usuario: ")
    password: str = getpass("Contraseña: ")
    print(user.create_new_user(username, password))

def set_difficulty() -> Board:
    """
    Sets the difficulty of the game.
    """
    menu_items: list[str] = ["Fácil", "Normal", "Difícil"]
    board = Board()
    board.difficulty = ask("Seleccione la dificultad:", menu_items)
    pairs_of_cards: int = 0

    match board.difficulty:
        case 0: pairs_of_cards = 8
        case 1: pairs_of_cards = 16
        case 2: pairs_of_cards = 26
        case _: pass

    board.fill(get_pairs_of_cards(pairs_of_cards))
    return board

def set_players_order() -> list[Player]:
    """
    Sets the order of the players.
    """
    number_of_players: int = 0

    while number_of_players > 4 or number_of_players < 2:
        number_of_players = int(input("Ingreses la cantidad de jugadores (2 a 4): "))

    print()
    verified_players: list[Player] = []

    for i in range(number_of_players):
        while True:
            print(f"Jugador {i + 1}:")
            username: str = input("Ingrese su usuario: ")
            password: str = getpass("Ingrese su contraseña: ")
            print()

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

    for i in range(len(players)): print(f"Turno {i + 1}: {players[i].username}")

    print()
    return players

def start(players: list[Player], board: Board) -> None:
    """
    Starts the game.
    """
    if not players:
        print("No se ha establecido el orden de los jugadores.")
        print("Por favor, seleccione la opción 2 y establezca el orden de los jugadores antes de iniciar el juego.\n")
        show_menu(players, board)

    print("Juego de memoria iniciado.\n")
    print("¡Buena suerte!\n")
    player_index_turn: int = 0

    while sum([player.score for player in players]) < len(board.cards) / 2:
        player = players[player_index_turn]

        print(f"Turno de «{player.username}»:\n")
        board.display()
        print(' | '.join([f"{player.username}: {player.score}" for player in players]))
        print()

        card_1_position: int = -1
        card_2_position: int = -1

        while card_1_position > len(board.cards) - 1 or card_1_position < 0:
            card_1_position: int = int(input("Ingrese la posición de la primera carta: ")) - 1

        while card_2_position > len(board.cards) - 1 or card_2_position < 0 or card_2_position == card_1_position:
            card_2_position: int = int(input("Ingrese la posición de la segunda carta: ")) - 1

        print()

        card_1 = board.cards[card_1_position]
        card_2 = board.cards[card_2_position]

        board.cards[card_1_position].is_visible = board.cards[card_2_position].is_visible = True
        board.display()

        if card_1.value == card_2.value and card_1.suit == card_2.suit:
            player.score += 1
            print("\n¡Cartas iguales! Ganaste un punto y tienes un turno adicional.\n")
        else:
            board.cards[card_1_position].is_visible = board.cards[card_2_position].is_visible = False
            print("\n¡Cartas diferentes! No ganaste ningún punto y tu turno ha finalizado.\n")
            player_index_turn = (player_index_turn + 1) % len(players)


if __name__ == "__main__":
    run()