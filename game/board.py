import card

board_difficulty: int = 0
cards_board: list[list] = [[]]
numbers_board: list[list] = [[]]

def generate_board(x: int, y: int) -> None:
    """Generates a board of dimensions "x" x "y", display in strings for simple assimilation.
    'x' represents amount of columns, and 'y' represents amount of rows"""

    global cards_board, numbers_board

    for i in range(0, y):
        cards_board.append(['[]'] * x)
        numbers_board.append(['[]'] * x)

def display_board(is_numbered: bool = False) -> None:
    """Displays the input board taking into account dimensional spaces."""

    for row in (cards_board if not is_numbered else numbers_board): print('    '.join(row))

def set_difficulty(difficulty: int):
    """Sets board dimensions based on chosen difficulty and instance.
        For difficulty: 0 = Easy, 1 = Normal, 2 = Hard."""

    global board_difficulty
    board_difficulty = difficulty

    match difficulty:
        case 0: generate_board(4, 4)
        case 1: generate_board(8, 4)
        case 2: generate_board(13, 4)

    fill_numbered_board()
    fill_board()

def fill_board() -> None:
    """Assigns respective keys to each individual element on board list.
        Does not include card 'values' (values = symbolic and numerical cards)."""

    step: int = 0
    number_of_different_cards: int = 0

    match board_difficulty:
        case 0: number_of_different_cards = 8
        case 1: number_of_different_cards = 16
        case 2: number_of_different_cards = 26

    card_pair: list[str] = card.get_cards(number_of_different_cards)

    for row in cards_board:
        for column in range(len(row)):
            row[column] = f"[ {card_pair[step]} ]"
            step += 1

def fill_numbered_board() -> None:
    i = 1

    for row in numbers_board:
        for column in range(len(row)):
            row[column] = f"[   {i}  ]" if i < 10 else f"[   {i} ]"
            i += 1

def show_match(card_1_position: int, card_2_position: int):
    position = 0

    for row in numbers_board:
        for column in row:
            position += 1
            if position == card_1_position or position == card_2_position:
                return