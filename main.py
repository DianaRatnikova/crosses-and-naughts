
from functions.constants import HELLO_MESSAGE, USER_ROLE, PROGRAM_ROLE, NAME_CROSSES, VICTORY, USERS_STEP, DRAW

from functions.game_board import fill_cell_in_game_board, show_game_board, make_game_board, game_board_is_full
from functions.program_coordinates import make_coord_for_program
from functions.roles import make_random_choice_of_roles, swich_player_for_next_step, decide_who_makes_next_step, swich_roles_for_next_step
from functions.user_coordinates import ask_and_make_coord_for_user, show_player_coord_tuple
from functions.victory import check_is_victory



if __name__ == "__main__":
    print(HELLO_MESSAGE)

    game_board_list = make_game_board()
    user_role, program_role = make_random_choice_of_roles()

    print(USER_ROLE, user_role)
    print(PROGRAM_ROLE, program_role)

    who_makes_next_step = decide_who_makes_next_step(user_role)
    current_role = NAME_CROSSES

    result_draw = False
    winner = ''
    
    while not check_is_victory(game_board_list):

        if game_board_is_full(game_board_list):
            print(DRAW)
            result_draw = True
            break

        if (who_makes_next_step == USERS_STEP):
            current_coord_tuple = ask_and_make_coord_for_user(game_board_list)
        else:
            current_coord_tuple = make_coord_for_program(game_board_list)

        show_player_coord_tuple(current_coord_tuple, current_role)
        game_board_list = fill_cell_in_game_board(game_board_list, current_coord_tuple, current_role)
        show_game_board(game_board_list)
        

        winner = who_makes_next_step
        who_makes_next_step = swich_player_for_next_step(who_makes_next_step)
        current_role = swich_roles_for_next_step(current_role)


    if not result_draw:
        print(VICTORY, ": ", winner)



