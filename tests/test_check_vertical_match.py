
from functions.victory import check_vertical_match
from functions.constants import NAME_EMPTY
import pytest


@pytest.mark.parametrize(
  "game_board_list, width_of_board, expected_result",
  [
    ([[NAME_EMPTY, NAME_EMPTY, NAME_EMPTY],[NAME_EMPTY, 'gert', NAME_EMPTY]], 3, False),
    ([[NAME_EMPTY, 'A', NAME_EMPTY],[NAME_EMPTY, 'A', NAME_EMPTY]], 3, True),
    ([[NAME_EMPTY, 'sfgb fg', 'NAME_EMPTY'],[NAME_EMPTY, 'A', 'NAME_EMPTY']], 3, True),
  ]      
)
def test__check_vertical_match__is_valid(game_board_list, width_of_board, expected_result):
    assert check_vertical_match(game_board_list, width_of_board) is expected_result


@pytest.mark.parametrize(
  "game_board_list, width_of_board, expected_error",
  [
    ([NAME_EMPTY, NAME_EMPTY, NAME_EMPTY], 3, TypeError),
  ]      
)
def test__check_vertical_match__errors(game_board_list, width_of_board, expected_error):
    with pytest.raises(expected_error):
        check_vertical_match(game_board_list, width_of_board)
