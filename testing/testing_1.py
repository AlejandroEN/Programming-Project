from card import *
from board_model import *

board = Board()
board.difficulty = 1
board.fill(get_pairs_of_cards(16))
board.display()