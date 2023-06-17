from board_model import Board

def display_board(is_numbered: bool = False) -> None:
    """Displays the input board taking into account dimensional spaces."""

    for row in (cards_board if not is_numbered else numbers_board): print('    '.join(row))

def display(board: Board) -> None:
    """Displays the input board taking into account dimensional spaces."""

    for row in board: print('    '.join(row))

def fill_board() -> None:
    """Assigns respective keys to each individual element on board list.
        Does not include card 'values' (values = symbolic and numerical cards)."""

    step: int = 0
    number_of_different_cards: int = 0

    match board_difficulty:
        case 0: number_of_different_cards = 8
        case 1: number_of_different_cards = 16
        case 2: number_of_different_cards = 26

    card_pair: list[str] = card.get_pairs_of_cards(number_of_different_cards)

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