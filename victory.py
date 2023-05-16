__author__ = 'DIANA'




# проверка строк: есть ли в одной строке 3 одинаковых символа
def check_horizontal_match(game_board_list):
    return False

# проверка столбцов: есть ли в одном столбце 3 одинаковых символа
def check_vertical_match(game_board_list):
    return False

# проверка главной диагонали: есть ли в ней 3 одинаковых символа
def check_main_diagonal_match(game_board_list):
    return False

# проверка побочной диагонали: есть ли в ней 3 одинаковых символа
def check_side_diagonal_match(game_board_list):
    return False

# проверка, есть ли победитель
def check_victory(game_board_list):
    victory_horizontal = check_horizontal_match(game_board_list)
    victory_vertical = check_vertical_match(game_board_list)
    victory_main_diagonal = check_main_diagonal_match(game_board_list)
    victory_side_diagonal = check_side_diagonal_match(game_board_list)

    is_victory = victory_horizontal or victory_vertical or victory_main_diagonal or victory_side_diagonal

    return is_victory
