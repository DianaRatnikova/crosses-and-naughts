from functions.constants import NAME_EMPTY, N
from typing import Any

def check_if_cell_is_empty(list_game_board: list[list[str | None]], 
                           player_coord_tuple: tuple[int, int]) -> bool:
    x = player_coord_tuple[0]
    y = player_coord_tuple[1]
    return list_game_board[x][y] == NAME_EMPTY


def check_coord_is_ok(coordinate: int|str) -> bool:
     return isinstance(coordinate, int) and coordinate >= 0 and coordinate <= N-1


def check_is_in_normal_range(player_coord_tuple: tuple[int|str, int|str]) -> bool:
    x = player_coord_tuple[0]
    y = player_coord_tuple[1]
    x_is_okay = check_coord_is_ok(x)
    y_is_okay = check_coord_is_ok(y)
    return x_is_okay and y_is_okay
