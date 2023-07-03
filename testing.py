from game import *

players: list[Player] = [Player("a"), Player("b")]

board = Board()
board.difficulty = 2
board.fill(get_pairs_of_cards(26))

start(players, board)


# set_players_order()