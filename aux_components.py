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

def initialize_game(difficulty:int, number_of_players:int, board:list):
    """Begins sequence for the game after selecting difficulty, number of players, and instance.
        For difficulty: 0 = Easy, 1 = Normal, 2 = Hard."""
    if difficulty == 0:
        return generate_board(4, 4)
    elif difficulty == 1:
        return generate_board(8, 4)
    elif difficulty == 2:
        return generate_board(13, 4)
    else:
        return print('Invalid difficult selected.')


B = generate_board(3, 2)
display_board(B)

status = (initialize_game(2, 0, 0))

B = status
display_board(B)








