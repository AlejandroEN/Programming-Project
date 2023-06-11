def ask(title: str, options: list[str]):
    print(f"{title}\n")
    for i in range(len(options)): print(f"{i + 1}. {options[i]}")
    print()

    while True:
        answer = int(input())
        print()

        if 1 <= answer <= len(options) + 1: break
        else: print("Elija un valor dentro del rango de opciones, por favor.\n")

    return answer - 1