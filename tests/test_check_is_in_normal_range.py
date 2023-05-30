from functions.coord_checks import check_is_in_normal_range
import pytest
from functions.constants import N


@pytest.mark.parametrize(
  "player_coord_tuple, expected_result",
  [
      ((0, 0), True),
      ((0, N),   False),
      ((N, 0),   False),
      ((0, N-1), True),
      ((N-1, 0), True),
      ((0, -1),   False),
      ((-1, 0),   False),
      ((0, '-1'),   False),
      (('-1', 0),   False),

  ]      
)
def test__check_is_in_normal_range__is_valid(player_coord_tuple, expected_result):
    assert check_is_in_normal_range(player_coord_tuple) is expected_result


def test__check_is_in_normal_range():
    with pytest.raises(TypeError):
        check_is_in_normal_range((0))