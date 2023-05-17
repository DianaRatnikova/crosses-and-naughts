import console_messages
import names

from game_board import fill_cell_in_game_board, show_game_board, make_game_board, game_board_is_full
from program_coordinates import make_coord_for_program
from roles import make_random_choice_of_roles, swich_player_for_next_step, decide_who_makes_next_step
from user_coordinates import ask_and_make_coord_for_user, show_player_coord_tuple
from victory import check_is_victory





if __name__ == "__main__":
    print(console_messages.HELLO_MESSAGE)

    game_board_list = make_game_board()
    user_role, program_role = make_random_choice_of_roles()

    print(console_messages.USER_ROLE, user_role)
    print(console_messages.PROGRAM_ROLE, program_role)

    who_makes_next_step = decide_who_makes_next_step(user_role)

    result_draw = False

    while not (check_is_victory(game_board_list)==True):
        if (who_makes_next_step == names.USERS_STEP):
            user_coord_tuple = ask_and_make_coord_for_user(game_board_list)
            show_player_coord_tuple(user_coord_tuple, user_role)
            game_board_list = fill_cell_in_game_board(game_board_list, user_coord_tuple, user_role)
        else:
            program_coord_tuple = make_coord_for_program(game_board_list)
            if not program_coord_tuple:
                print(console_messages.ALL_CELLS_OCCUPIED)
                print(console_messages.DRAW)
                result_draw = True
                break
            show_player_coord_tuple(program_coord_tuple, program_role)
            game_board_list = fill_cell_in_game_board(game_board_list, program_coord_tuple, program_role)
        show_game_board(game_board_list)
        if game_board_is_full(game_board_list):
            print(console_messages.DRAW)
            result_draw = True
            break
        winner = who_makes_next_step
        who_makes_next_step = swich_player_for_next_step(who_makes_next_step)
        
    if not result_draw:
        print(console_messages.VICTORY, ": ", winner)



