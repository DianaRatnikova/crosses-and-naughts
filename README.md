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