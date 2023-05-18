

import constants
from coord_checks import check_is_in_normal_range, check_if_cell_is_empty


def take_one_coord_from_user(coord_name: str):# -> int|str:
    try:
        coord = int(input("\nenter "+ coord_name + ": "))
    except ValueError:
        coord = 10
    return coord

def ask_coord_for_user() -> tuple:
    x = take_one_coord_from_user("horizontal")
    y = take_one_coord_from_user("vertical")
    return (x,y)


def ask_and_make_coord_for_user(game_board_list: list) -> tuple:
    while True:
        user_coord_tuple = ask_coord_for_user()
        if (check_is_in_normal_range(user_coord_tuple)):
            if check_if_cell_is_empty(game_board_list, user_coord_tuple):
                return user_coord_tuple
            else:
                print(constants.CELL_IS_OCCUPIED)
        else:
            print(constants.OUT_OF_RANGE)


def show_player_coord_tuple(player_coord_tuple: tuple, player_role: str) -> None:
    print("\n" + player_role, " ( ", player_coord_tuple[0], ", ", player_coord_tuple[1], ")")