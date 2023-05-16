__author__ = 'DIANA'

import names


def check_if_cell_is_empty(list_game_board, player_coord_dict):
    x = player_coord_dict["horizontal"] - 1
    y = player_coord_dict["vertical"] - 1

    if list_game_board[x][y] == names.NAME_EMPTY:
        return True
    return False


def check_coord_is_ok(coord):
    if isinstance(coord, int):
        if (coord>=0) and (coord<=2):
            return True
    return False


def check_is_in_normal_range(player_coord_dict):
    x = player_coord_dict["horizontal"] - 1
    y = player_coord_dict["vertical"] - 1
    x_is_okay = check_coord_is_ok(x)
    y_is_okay = check_coord_is_ok(y)
    if x_is_okay and y_is_okay:
        return True
    return False
