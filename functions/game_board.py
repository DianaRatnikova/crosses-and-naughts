
from functions.constants import N, NAME_EMPTY
from typing import Any

def make_game_board() -> list[list[str|None]]:
    game_board_list: list[list[str|None]]
    game_board_list = [[NAME_EMPTY] * N for i in range(N)]
    return game_board_list

def show_game_board(list_game_board: list[list[str|None]]) -> None:
    for row in list_game_board:
        print(row)


def fill_cell_in_game_board(game_board_list: list[list[str|None]], 
                            player_coord_tuple: tuple[int,int], 
                            player_role: str) -> list[list[str|None]]:
    x = player_coord_tuple[0]
    y = player_coord_tuple[1]
    game_board_list[x][y] = player_role
    return game_board_list


def game_board_is_full(game_board_list: list[list[str|None]]) -> bool:
    for row in game_board_list:
        for cell in row:
            if cell == NAME_EMPTY:
                return False
    return True