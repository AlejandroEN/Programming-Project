from board_model import Board

def display_board(is_numbered: bool = False) -> None:
    """Displays the input board taking into account dimensional spaces."""

    for row in (cards_board if not is_numbered else numbers_board): print('    '.join(row))

def display(board: Board) -> None:
    """Displays the input board taking into account dimensional spaces."""

    for row in board: print('    '.join(row))