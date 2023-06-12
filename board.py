import card

board_difficulty: int = 0

def generate_board(x: int, y: int):
    """Generates a board of dimensions "x" x "y", display in strings for simple assimilation.
    'x' represents amount of columns, and 'y' represents amount of rows"""

    board: list[str] = []
    total_numbers: int = x * y
    visual_board: str = ''

    for i in range(0, y): board.append(f'[ ]' * x)

    return board

def display_board(board: list):
    """Displays the board taking into account dimensional spaces."""

    for row in board: print(' '.join(row))

def set_difficulty(difficulty: int):
    """Sets board dimensions based on chosen difficulty and instance.
        For difficulty: 0 = Easy, 1 = Normal, 2 = Hard."""

    match difficulty:
        case 0:
            return generate_board(4, 4)
        case 1: return generate_board(8, 4)
        case 2: return generate_board(13, 4)
        case _: print("Invalid difficult selected.")  # Use throw

def fill_board(board: list):
    """Assigns respective keys to each individual element on board list.
        Does not include card 'values' (values = symbolic and numerical cards)."""
    u = 0
    card_pair = card.get_cards(8)
    for i in range(len(board)):
        board[i] = f"[{card_pair[u]}] [{card_pair[u+1]}] [{card_pair[u+2]}] [{card_pair[u+3]}]"
        u += 4
