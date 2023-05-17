import names


def check_if_list_of_equal_elements(list_to_check: list)-> bool:
    set_from_list = set(list_to_check)
    return len(set_from_list) == 1


# проверка строк: есть ли в одной строке 3 одинаковых символа
def check_horizontal_match(game_board_list: list)->bool:
    for stroka in game_board_list:
        if stroka[0] == names.NAME_EMPTY:
            break
        if check_if_list_of_equal_elements(stroka):
            return True
    return False


# проверка столбцов: есть ли в одном столбце 3 одинаковых символа
def check_vertical_match(game_board_list: list)->bool:
    for stolb_num in range(3):
        stolb = [stroka[stolb_num] for stroka in game_board_list]
        if stolb[0]== names.NAME_EMPTY:
            break
        if check_if_list_of_equal_elements(stolb):
            return True
    return False


# проверка главной диагонали: есть ли в ней 3 одинаковых символа
def check_main_diagonal_match(game_board_list: list)->bool:
    for i in range(0,2):
        if game_board_list[i][i] ==  names.NAME_EMPTY:
            return False
        if game_board_list[i][i]!= game_board_list[i+1][i+1]:
            return False
    return True


# проверка побочной диагонали: есть ли в ней 3 одинаковых символа
def check_side_diagonal_match(game_board_list: list)->bool:
    for i in range(0,2):
        if game_board_list[i][2-i] ==  names.NAME_EMPTY:
            return False
        if game_board_list[i][2-i]!= game_board_list[i+1][1-i]:
            return False
    return True


# проверка, есть ли победитель
def check_is_victory(game_board_list: list)->bool:
    victory_horizontal = check_horizontal_match(game_board_list)
    victory_vertical = check_vertical_match(game_board_list)
    victory_main_diagonal = check_main_diagonal_match(game_board_list)
    victory_side_diagonal = check_side_diagonal_match(game_board_list)
    is_victory = victory_horizontal or victory_vertical or victory_main_diagonal or victory_side_diagonal

    return is_victory
