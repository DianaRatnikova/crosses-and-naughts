
from functions.victory import check_vertical_match
from functions.constants import NAME_EMPTY
import pytest


@pytest.mark.parametrize(
  "game_board_list, expected_result",
  [
    ([[NAME_EMPTY, NAME_EMPTY, NAME_EMPTY],[NAME_EMPTY, 'gert', NAME_EMPTY]], False),
    ([[NAME_EMPTY, 'A', NAME_EMPTY],[NAME_EMPTY, 'A', NAME_EMPTY]], True),
    ([[NAME_EMPTY, 'sfgb fg', 'NAME_EMPTY'],[NAME_EMPTY, 'A', 'NAME_EMPTY']], True),
  ]      
)
def test__check_vertical_match__is_valid(game_board_list, expected_result):
    assert check_vertical_match(game_board_list) is expected_result


@pytest.mark.parametrize(
  "game_board_list, expected_error",
  [
    ([NAME_EMPTY, NAME_EMPTY, NAME_EMPTY], TypeError),
  ]      
)
def test__check_vertical_match__errors(game_board_list, expected_error):
    with pytest.raises(expected_error):
        check_vertical_match(game_board_list)
