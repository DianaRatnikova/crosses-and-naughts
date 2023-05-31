
from functions.constants import WIDTH_OF_BOARD
from functions.coord_checks import check_is_in_normal_range
import pytest


@pytest.mark.parametrize(
  "player_coord_tuple, expected_result",
  [
      ((0, 0), True),
      ((0, WIDTH_OF_BOARD),   False),
      ((WIDTH_OF_BOARD, 0),   False),
      ((0, WIDTH_OF_BOARD - 1), True),
      ((WIDTH_OF_BOARD - 1, 0), True),
      ((0, -1),   False),
      ((-1, 0),   False),
      ((0, '-1'),   False),
      (('-1', 0),   False),

  ]      
)
def test__check_is_in_normal_range__is_valid(player_coord_tuple, expected_result):
    assert check_is_in_normal_range(player_coord_tuple) is expected_result


def test__check_is_in_normal_range__typeerror():
    with pytest.raises(TypeError):
        check_is_in_normal_range((0))