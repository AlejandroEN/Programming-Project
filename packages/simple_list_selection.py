def ask(title: str, options: list[str]) -> int:
    """
    Ask the user to choose an option from a list of options.
    """
    print(f"{title}\n")
    for i in range(len(options)): print(f"{i + 1}. {options[i]}")
    print()

    while True:
        try:
            answer: int = int(input("Ingrese la opción deseada: "))
            if 1 <= answer <= len(options): break
            else: raise ValueError
        except ValueError:
            print("Elija un valor dentro del rango de opciones, por favor.\n")

    print()
    return answer - 1