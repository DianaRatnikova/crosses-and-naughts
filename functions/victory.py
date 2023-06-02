from functions.constants import WIDTH_OF_BOARD, NAME_EMPTY


def check_if_list_of_equal_elements(
        list_to_check: list[str | None]
        ) -> bool:
    set_from_list = set(list_to_check)
    return len(set_from_list) == 1


def check_horizontal_match(game_board_list):
    for row in game_board_list:
        if row[0] != NAME_EMPTY:
            if check_if_list_of_equal_elements(row):
                return True
    return False


def check_vertical_match(game_board_list, width_of_board: int):
    for column_num in range(width_of_board):
        column = [row[column_num] for row in game_board_list]
        if column[0] != NAME_EMPTY and check_if_list_of_equal_elements(column):
            return True
    return False


def check_main_diagonal_match(
        game_board_list: list[list[str | None]],
        width_of_board: int
        ) -> bool:
    for string_num in range(width_of_board - 1):
        if game_board_list[string_num][string_num] ==  NAME_EMPTY:
            return False
        if game_board_list[string_num][string_num] != game_board_list[string_num + 1][string_num + 1]:
            return False
    return True


def check_side_diagonal_match(
        game_board_list: list[list[str | None]],
        width_of_board: int
        ) -> bool:
    summ_of_index = width_of_board - 1
    for string_num in range(summ_of_index):
        if game_board_list[string_num][summ_of_index - string_num] ==  NAME_EMPTY:
            return False
        if game_board_list[string_num][summ_of_index - string_num] != game_board_list[string_num + 1][summ_of_index - 1 - string_num]:
            return False
    return True


def check_is_victory(
        game_board_list: list[list[str | None]]
        ) -> bool:
    victory_horizontal = check_horizontal_match(game_board_list)
    victory_vertical = check_vertical_match(game_board_list, WIDTH_OF_BOARD)
    victory_main_diagonal = check_main_diagonal_match(game_board_list, WIDTH_OF_BOARD)
    victory_side_diagonal = check_side_diagonal_match(game_board_list, WIDTH_OF_BOARD)
    is_victory = victory_horizontal or victory_vertical or victory_main_diagonal or victory_side_diagonal

    return is_victory
