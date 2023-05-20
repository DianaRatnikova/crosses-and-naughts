
import random
import constants
from coord_checks import check_if_cell_is_empty


def take_one_coord_from_program() -> int:
    coord = random.randint(0, constants.N-1)
    return coord


def take_coord_for_program() -> tuple[int,int]:
    x = take_one_coord_from_program()
    y = take_one_coord_from_program()
    return x, y


def make_coord_for_program(game_board_list: list[list[str|None]]) -> tuple[int, int]:
    while True:
        program_coord_tuple = take_coord_for_program()
        if check_if_cell_is_empty(game_board_list, program_coord_tuple):
            return program_coord_tuple
        else:
            print(constants.CELL_IS_OCCUPIED, ": program tried", program_coord_tuple)


        
