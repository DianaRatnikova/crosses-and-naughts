__author__ = 'DIANA'

from coord_checks import check_is_in_normal_range, check_if_cell_is_empty

def make_empty_coord_dict():
    coord_dict = {"symbol": "Empty", "horizontal": 0, "vertical": 0}
    return coord_dict


def take_one_coord_from_user(coord_name):
    coord = int(input("\nenter "+ coord_name + ": "))
    return coord


def ask_coord_for_user(user_r):
    user_coord_dict = make_empty_coord_dict()
    user_coord_dict["symbol"] = user_r
    user_coord_dict["horizontal"] = take_one_coord_from_user("horizontal")
    user_coord_dict["vertical"] = take_one_coord_from_user("vertical")
    return user_coord_dict



def make_coord_for_user(user_role, game_board_list):
    while True:
        user_coord_dict = ask_coord_for_user(user_role)
        if (check_is_in_normal_range(user_coord_dict)):
            if check_if_cell_is_empty(game_board_list, user_coord_dict):
                return user_coord_dict
            else:
                print("Клетка занята!")
        else:
            print("Вы вышли за диапазон!")


def show_player_coord_dict(player_coord_dict):
    print(player_coord_dict["symbol"], " ( ", player_coord_dict["horizontal"], ", ", player_coord_dict["vertical"], ")")