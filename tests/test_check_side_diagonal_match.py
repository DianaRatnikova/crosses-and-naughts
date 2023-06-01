from functions.victory import check_side_diagonal_match
from functions.constants import NAME_EMPTY
import pytest


# Вопрос: возможно ли написать для функции eck_side_diagonal_match
# универсальный тест?
# сейчас тесты привязаны к размерности 3 на з, но она может меняться в файле constants.py

@pytest.mark.parametrize(
  "game_board_list, expected_result",
  [
 #   ([[NAME_EMPTY, NAME_EMPTY], [NAME_EMPTY, NAME_EMPTY]], False),
    ([[0, NAME_EMPTY, NAME_EMPTY], 
    [NAME_EMPTY, 0, NAME_EMPTY], 
    [NAME_EMPTY, NAME_EMPTY, 0]], 
    False),
    ([['A', NAME_EMPTY, NAME_EMPTY], 
    [NAME_EMPTY, 'A', NAME_EMPTY], 
    [NAME_EMPTY, NAME_EMPTY, 'A']], 
    False),
    ([['A', NAME_EMPTY, NAME_EMPTY], 
    [NAME_EMPTY, 'B', NAME_EMPTY], 
    [NAME_EMPTY, NAME_EMPTY, 'A']], 
    False),
    ([['A', NAME_EMPTY, 'A'], 
    [NAME_EMPTY, 'A', NAME_EMPTY], 
    ['A', NAME_EMPTY, 'A']], 
    True),
  ]      
)
def test__check_side_diagonal_match__is_valid(game_board_list, expected_result):
    assert check_side_diagonal_match(game_board_list) is expected_result


@pytest.mark.parametrize(
  "game_board_list, expected_error",
  [
    ([], IndexError),
    ([NAME_EMPTY, NAME_EMPTY, NAME_EMPTY], TypeError),
    ('A', IndexError)
  ]      
)
def test__check_side_diagonal_match__errors(game_board_list, expected_error):
    with pytest.raises(expected_error):
        check_side_diagonal_match(game_board_list)

