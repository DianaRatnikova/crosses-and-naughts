__author__ = 'DIANA'

import names

# Создание списка с пустыми метками
def make_game_board():
    game_board_list = [[names.NAME_EMPTY]*3 for i in range(3)]
    return game_board_list


def show_game_board(list_game_board):
    for horizontal_line in list_game_board:
        print(horizontal_line)
#Вывод текущего состояния игровой доски


def fill_cell_in_game_board(self, player_coord_dict):
    x = player_coord_dict["horizontal"] - 1
    y = player_coord_dict["vertical"] - 1
    self[x][y] = player_coord_dict["symbol"]
    return self
