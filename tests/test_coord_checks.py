from functions.coord_checks import check_coord_is_ok
from functions.coord_checks import check_if_cell_is_empty
from functions.coord_checks import check_is_in_normal_range
from functions.constants import WIDTH_OF_BOARD
import pytest


@pytest.mark.parametrize(
    "list_game_board, player_coord_tuple, expected_result",
    [
        ([[None, None, None], [None, None, None], [None, None, None]], (0, 0), True),
        ([["jhhv", None, None], [None, None, None], [None, None, None]], (0, 0), False),
    ]
)
def test__check_if_cell_is_empty__is_valid(list_game_board, player_coord_tuple, expected_result):
    assert check_if_cell_is_empty(list_game_board, player_coord_tuple) == expected_result


def test__check_if_cell_is_empty__indexerror():
    with pytest.raises(IndexError):
        check_if_cell_is_empty([["jhhv", None, None], [None, None, None], [None, None, None]], (9,1))


@pytest.mark.parametrize(
  "coord, expected_result",
  [
      (WIDTH_OF_BOARD - 1, True),
      (0, True),
      (-1, False),
      (WIDTH_OF_BOARD + 1, False),
      ('werdf', False),

  ]      
)
def test__check_coord_is_ok__is_valid(coord, expected_result):
    assert check_coord_is_ok(coord) is expected_result


@pytest.mark.parametrize(
  "player_coord_tuple, expected_result",
  [
      ((0, 0), True),
      ((0, WIDTH_OF_BOARD),   False),
      ((WIDTH_OF_BOARD, 0),   False),
      ((0, WIDTH_OF_BOARD-1), True),
      ((WIDTH_OF_BOARD-1, 0), True),
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