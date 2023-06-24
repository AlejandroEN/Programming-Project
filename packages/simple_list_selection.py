def ask(title: str, options: list[str]) -> int:
    print(f"{title}\n")
    for i in range(len(options)): print(f"{i + 1}. {options[i]}")
    print()

    while True:
        answer: int = int(input("Ingrese la opción deseada: "))
        print()

        if 1 <= answer <= len(options): break
        else: print("Elija un valor dentro del rango de opciones, por favor.\n")

    return answer - 1