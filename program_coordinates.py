__author__ = 'DIANA'

import random
from coord_checks import check_if_cell_is_empty
from user_coordinates import make_empty_coord_dict


def take_one_coord_from_program():
    coord = random.randint(1, 3)
    return coord


def take_coord_for_program(program_r):
    program_coord_dict = make_empty_coord_dict()
    program_coord_dict["symbol"] = program_r
    program_coord_dict["horizontal"] = take_one_coord_from_program()
    program_coord_dict["vertical"] = take_one_coord_from_program()
    return program_coord_dict



def make_coord_for_program(program_role, game_board_list):
    while True:
        program_coord_dict = take_coord_for_program(program_role)
        if check_if_cell_is_empty(game_board_list, program_coord_dict):
            return program_coord_dict
        else:
            print("Клетка занята!")