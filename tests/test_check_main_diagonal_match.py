from functions.victory import check_main_diagonal_match
from functions.constants import NAME_EMPTY
import pytest


@pytest.mark.parametrize(
  "game_board_list, width_of_board, expected_result",
  [
    ([[NAME_EMPTY, NAME_EMPTY], [NAME_EMPTY, NAME_EMPTY]], 3, False),
    ([[0, NAME_EMPTY, NAME_EMPTY], 
    [NAME_EMPTY, 0, NAME_EMPTY], 
    [NAME_EMPTY, NAME_EMPTY, 0]], 
    3,
    True),
    ([['A', NAME_EMPTY, NAME_EMPTY], 
    [NAME_EMPTY, 'A', NAME_EMPTY], 
    [NAME_EMPTY, NAME_EMPTY, 'A']], 
    3,
    True),
    ([['A', NAME_EMPTY, NAME_EMPTY], 
    [NAME_EMPTY, 'B', NAME_EMPTY], 
    [NAME_EMPTY, NAME_EMPTY, 'A']], 
    3,
    False),
  ]      
)
def test__check_main_diagonal_match__is_valid(game_board_list, width_of_board, expected_result):
    assert check_main_diagonal_match(game_board_list, width_of_board) is expected_result


@pytest.mark.parametrize(
  "game_board_list, width_of_board, expected_error",
  [
    ([], 3, IndexError),
    ([NAME_EMPTY, NAME_EMPTY, NAME_EMPTY], 3, TypeError),
  ]      
)
def test__check_main_diagonal_match__errors(game_board_list, width_of_board, expected_error):
    with pytest.raises(expected_error):
        check_main_diagonal_match(game_board_list, width_of_board)

 
