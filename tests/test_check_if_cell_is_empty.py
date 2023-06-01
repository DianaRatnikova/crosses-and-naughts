from functions.coord_checks import check_if_cell_is_empty
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


