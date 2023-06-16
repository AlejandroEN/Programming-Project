import card

board_difficulty: int = 0

def generate_board(x: int, y: int) -> list[list]:
    """Generates a board of dimensions "x" x "y", display in strings for simple assimilation.
    'x' represents amount of columns, and 'y' represents amount of rows"""

    board_list: list[list] = []
    for i in range(0, y): board_list.append(['[]'] * x)
    return board_list

def display_board(board: list) -> None:
    """Displays the board taking into account dimensional spaces."""

    for row in board: print(' '.join(row))

def set_difficulty(difficulty: int) -> list[list]:
    """Sets board dimensions based on chosen difficulty and instance.
        For difficulty: 0 = Easy, 1 = Normal, 2 = Hard."""

    global board_difficulty

    match difficulty:
        case 0: return generate_board(4, 4)
        case 1: return generate_board(8, 4)
        case 2: return generate_board(13, 4)
        case _: print("Invalid difficult selected.")  # Use throw

    board_difficulty = difficulty

def fill_board(board: list) -> None:
    """Assigns respective keys to each individual element on board list.
        Does not include card 'values' (values = symbolic and numerical cards)."""

    step: int = 0
    n: int = 0

    match board_difficulty:
        case 0: n = 8
        case 1: n = 16
        case 2: n = 26
        case _: print('System error.')

    card_pair: list[str] = card.get_cards(n)

    for row in board:
        for column in range(0, len(row)):
            row[column] = f"[{card_pair[step]}]"
            step += 1

    step += 4