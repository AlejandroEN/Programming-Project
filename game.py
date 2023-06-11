from simple_list_selection import ask
from getpass import getpass
from user import create_new_user

def show_welcome():
    welcome = "This is a welcome"
    print(f"{welcome}\n")

def show_first_menu():
    first_menu_items = ["Registrar jugador", "Establecer nuevo jugador", "Iniciar juego de memoria", "Salir"]

    choice = ask("Seleccione una de las siguientes opciones:", first_menu_items)

    match choice:
        case 0: show_create_new_user()

def show_create_new_user():
    username = input("Usuario: ")
    password = getpass("Contraseña: ")
    create_new_user(username, password)
    show_first_menu()