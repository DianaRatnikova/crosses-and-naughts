

import console_messages
import names
import random

from game_board import fill_cell_in_game_board, show_game_board, make_game_board
from program_coordinates import make_coord_for_program
from user_coordinates import make_coord_for_user, show_player_coord_dict
from victory import check_victory


def make_user_and_program_roles():
    roles = [names.NAME_NAUGHTS, names.NAME_CROSSES]
    user_r, program_r = random.sample(roles, 2)
    return user_r, program_r


if __name__ == "__main__":
    print(console_messages.HELLO_MESSAGE)

    game_board_list = make_game_board()

# рандомно определяем, кто за крестики, кто за нолики
    user_role, program_role = make_user_and_program_roles()

    print("user_role    = ", user_role)
    print("program_role = ", program_role)

    for count in range(4):
        user_coord_dict = make_coord_for_user(user_role, game_board_list)
        show_player_coord_dict(user_coord_dict)

        game_board_list = fill_cell_in_game_board(game_board_list, user_coord_dict)

        if (check_victory(game_board_list)):
            print("Победа!:")
            break

        show_game_board(game_board_list)

        program_coord_dict = make_coord_for_program(program_role, game_board_list)
        show_player_coord_dict(program_coord_dict)

        game_board_list = fill_cell_in_game_board(game_board_list, program_coord_dict)

        if (check_victory(game_board_list)):
            print("Победа!:")
            break

        show_game_board(game_board_list)



