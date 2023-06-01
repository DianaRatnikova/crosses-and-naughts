from functions.constants import NAME_EMPTY
from functions.victory import check_horizontal_match
import pytest

@pytest.mark.parametrize(
  "game_board_list, expected_result",
  [
     ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], True),
    ([[NAME_EMPTY, 1, 1], [1, 1, 1], [1, 1, 1]], True),
    ([[NAME_EMPTY, NAME_EMPTY, NAME_EMPTY], [NAME_EMPTY, NAME_EMPTY, NAME_EMPTY], [NAME_EMPTY, NAME_EMPTY, NAME_EMPTY]], False),
  ]      
)
def test__check_horizontal_match__is_valid(game_board_list, expected_result):
    assert check_horizontal_match(game_board_list) is expected_result


@pytest.mark.parametrize(
  "game_board_list, expected_error",
  [
 #   ([[NAME_EMPTY, NAME_EMPTY, NAME_EMPTY]], NameError),
    ([NAME_EMPTY, NAME_EMPTY, NAME_EMPTY], TypeError),
  ]      
)
def test__check_horizontal_match__errors(game_board_list, expected_error):
    with pytest.raises(expected_error):
        check_horizontal_match(game_board_list)