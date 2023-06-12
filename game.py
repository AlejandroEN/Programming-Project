from simple_list_selection import ask
from getpass import getpass
from user import create_new_user, check_user
from board import set_difficulty

def show_welcome():
    welcome = "This is a welcome"
    print(f"{welcome}\n")

def show_first_menu():
    menu_items = ["Registrar jugador", "Establecer turno", "Iniciar juego de memoria", "Salir"]
    choice = ask("Seleccione una de las siguientes opciones:", menu_items)

    match choice:
        case 0: show_create_new_user()
        case 1:
            show_set_difficulty()
            set_players_order()
        case 2: run_memory_game()
        case 4: return

def show_create_new_user():
    username = input("Usuario: ")
    password = getpass("Contraseña: ")
    create_new_user(username, password)
    show_first_menu()

def show_set_difficulty():
    menu_items = ["Fácil", "Normal", "Difícil"]
    choice = ask("Seleccione la dificultad:", menu_items)
    set_difficulty(choice)

def set_players_order():
    number_of_players = 0
    while number_of_players > 4 or number_of_players < 2: number_of_players = int(input("Ingreses la cantidad de jugadores (2 a 4): "))
    print()

    for i in range(number_of_players):
        while True:
            print(f"Jugador {i + 1}:")
            username = input("Ingrese su usuario: ")
            password = getpass("Ingrese su contraseña: ")

            if check_user(username, password): break
            else: print("Usuario o contraseña incorrectos. Intente de nuevo, por favor.\n")

        print()


def run_memory_game():
    return