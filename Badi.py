def generate_board(x: int, y: int):
    """Generates board of dimensions "x" x "y", display in strings for simple assimilation.
    'x' represents amount of columns, and 'y' represents amount of rows"""
    board = []
    total_nums = x * y

    visual_board = ''
    for i in range(0, y):
        row = f'[ ]' * x
        board.append(row)
    return board

def display_board(board: list):
    """Displays the board taking into account dimensional spaces."""
    for row in board:
        print(' '.join(row))

def set_board_difficulty(difficulty: int):
    """Makes board modification after selecting difficulty, number of players, and instance.
        For difficulty: 0 = Easy, 1 = Normal, 2 = Hard."""
    if difficulty == 0:
        board = generate_board(4, 4)
        return board
    elif difficulty == 1:
        board = generate_board(8, 4)
        return board
    elif difficulty == 2:
        board = generate_board(13, 4)
        return board
    else:
        return print('Invalid difficult selected.')

def set_cards_difficulty(difficulty: int, board: list):
    return 1

B = generate_board(3, 2)
display_board(B)

set_board_difficulty(2, B)

display_board(B)








