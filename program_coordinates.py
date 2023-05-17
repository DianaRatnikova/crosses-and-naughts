
import random
import console_messages
from coord_checks import check_if_cell_is_empty


def take_one_coord_from_program()->int:
    coord = random.randint(0, 2)
    return coord


def take_coord_for_program() -> tuple:
    x = take_one_coord_from_program()
    y = take_one_coord_from_program()
    return (x, y)


def make_coord_for_program(game_board_list: list) -> tuple|None:
    total_number_of_cells = 9
    for i in range(1, total_number_of_cells):
        program_coord_tuple = take_coord_for_program()
        if check_if_cell_is_empty(game_board_list, program_coord_tuple):
            return program_coord_tuple
        else:
            print(console_messages.CELL_IS_OCCUPIED)
    return None
        
