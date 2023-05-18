# crosses-and-naughts
Консольная игра в крестики-нолики

Изменения 17.05.2023:
1. make_random_choice_of_roles - новое имя функции
2. в этой функции убрала сокращения в переменных user_role, user_role
3. Координатыи теперь начинаются с нуля
4. В def check_coord_is_ok(coord) заменила два if на and and
5.     if x_is_okay and y_is_okay:
        return True
    return False
    
    в check_is_in_normal_range
    заменила на 
    return x_is_okay and y_is_okay:
    
6. В def make_coord_for_program(program_role, game_board_list):
заменила цикл
    while True
на    
for i in range(1, total_number_of_cells):
total_number_of_cells = 9 - общее количество клеток на поле
7. Заменила все словари на тюплы
8. Добавила функции на определение победы в модуле victory
9. Изменила логику проведния игры в цикле
10. Добавила аннотацию типов


Изменения 18/05/2023
1. форматирование кода сломалось - починю
2. добавила в gotignore .idea
3. В main.py теперь
 while not (check_is_victory(game_board_list)) вместо  while not (check_is_victory(game_board_list) == True)
4. Убрала повтор в ветках if
    #    show_player_coord_tuple(current_coord_tuple, current_role)
    #    game_board_list = fill_cell_in_game_board(game_board_list, current_coord_tuple, current_role)

5. Убрала дубликат обработки ничьей из главного цикла:
    #    if not current_coord_tuple:
    #        print(console_messages.ALL_CELLS_OCCUPIED)
    #        print(console_messages.DRAW)
    #        result_draw = True
    #        break
6. Аннотация типов: как указать список списков???
7. Убрала транслит :)
8. names.py и console_messages.py объединила в constants.py
9.     for i in range(1, total_number_of_cells): заменила на     for _ in range(1, total_number_of_cells):
Тк к не использую переменную i
Не использовать однобуквенные названия в счётчиках!