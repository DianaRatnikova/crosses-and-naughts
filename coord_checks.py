import constants


def check_if_cell_is_empty(list_game_board: list, player_coord_tuple: tuple) -> bool:
    x = player_coord_tuple[0]
    y = player_coord_tuple[1]
    return list_game_board[x][y] == constants.NAME_EMPTY


def check_coord_is_ok(coordinate) -> bool:
    return isinstance(coordinate, int) and coordinate >= 0 and coordinate <= 2


def check_is_in_normal_range(player_coord_tuple : tuple) -> bool:
    x = player_coord_tuple[0]
    y = player_coord_tuple[1]
    x_is_okay = check_coord_is_ok(x)
    y_is_okay = check_coord_is_ok(y)
    return x_is_okay and y_is_okay
