
import names

# Создание списка с пустыми метками
def make_game_board() -> list:
    game_board_list = [[names.NAME_EMPTY]*3 for i in range(3)]
    return game_board_list


def show_game_board(list_game_board: list) -> None:
    for horizontal_line in list_game_board:
        print(horizontal_line)
#Вывод текущего состояния игровой доски


def fill_cell_in_game_board(game_board_list: list, player_coord_tuple: tuple, player_role: str)->list:
    x = player_coord_tuple[0]
    y = player_coord_tuple[1]
    game_board_list[x][y] = player_role
    return game_board_list


def game_board_is_full(game_board_list: list) ->bool:
    for stroka in game_board_list:
        for cell in stroka:
            if cell == names.NAME_EMPTY:
                return False
    return True