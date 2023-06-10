import random

def gen_board(x: int, y: int):
    """Generates board of dimensions "x" x "y", display in strings for simple assimilation"""
    board = []
    for i in range(0, y):
        row = f'[.]' * x
        board.append(row)
    return board

def display_board(board: list):
    """Displays the board taking into account dimensional spaces."""
    for row in board:
        print(' '.join(row))

def fill_board(board: list):
    total_nums = x * y




