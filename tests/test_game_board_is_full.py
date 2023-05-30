from functions.game_board import game_board_is_full
import pytest


@pytest.mark.parametrize(
    "game_board_list, expected_result",
    [
        ([[None, None, None], [None, None, None], [None, None, None]], False),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], True),
    ]
)
def test__game_board_is_full__is_valid(game_board_list, expected_result):
    assert game_board_is_full(game_board_list) == expected_result