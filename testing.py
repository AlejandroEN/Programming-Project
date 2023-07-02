from game import *

players: list[Player] = [Player("a"), Player("b"), Player("c"), Player("d")]

board = Board()
board.difficulty = 3
board.fill(get_pairs_of_cards(26))

start(players, board)