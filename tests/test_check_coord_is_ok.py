from functions.constants import WIDTH_OF_BOARD
from functions.coord_checks import check_coord_is_ok
import pytest


@pytest.mark.parametrize(
  "coord, expected_result",
  [
      (WIDTH_OF_BOARD - 1, True),
      (0, True),
      (-1, False),
      (WIDTH_OF_BOARD + 1, False),
  ]      
)
def test__check_coord_is_ok__is_valid(coord, expected_result):
    assert check_coord_is_ok(coord) is expected_result

@pytest.mark.parametrize(
  "coord, expected_error",
  [
    ('werdf', TypeError),
  ]      
)
def test__check_coord_is_ok_errors(coord, expected_error):
    with pytest.raises(expected_error):
        check_coord_is_ok(coord)