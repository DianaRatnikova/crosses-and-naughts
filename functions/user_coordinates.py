
from functions.constants import N, CELL_IS_OCCUPIED, OUT_OF_RANGE
from functions.coord_checks import check_is_in_normal_range, check_if_cell_is_empty


def take_one_coord_from_user(coord_name: str) -> int:
    try:
        coord = int(input("\nenter "+ coord_name + ": "))
    except ValueError:
        coord = N+1
    return coord

def ask_coord_for_user() -> tuple[int, int]:
    x = take_one_coord_from_user("horizontal")
    y = take_one_coord_from_user("vertical")
    return x,y


def ask_and_make_coord_for_user(game_board_list: list[list[str|None]]) -> tuple[int, int]:
    while True:
        user_coord_tuple = ask_coord_for_user()
        if (check_is_in_normal_range(user_coord_tuple)):
            if check_if_cell_is_empty(game_board_list, user_coord_tuple):
                return user_coord_tuple
            else:
                print(CELL_IS_OCCUPIED)
        else:
            print(OUT_OF_RANGE)


def show_player_coord_tuple(player_coord_tuple: tuple[int,int], player_role: str) -> None:
    print("\n" + player_role, " ( ", player_coord_tuple[0], ", ", player_coord_tuple[1], ")")