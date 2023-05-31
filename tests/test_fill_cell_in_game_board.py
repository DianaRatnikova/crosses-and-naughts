from functions.game_board import fill_cell_in_game_board
import pytest


@pytest.mark.parametrize(
  "game_board_list, player_coord_tuple, player_role, expected_result",
  [
      ([[None, None, None], [None, None, None], [None, None, None]], 
       (0, 0), 'Crosses', 
       [['Crosses', None, None], [None, None, None], [None, None, None]]),
      ([[None, None, None], [None, None, None], [None, None, None]], 
       (0, 1), 'Crosses', 
       [[None, 'Crosses', None], [None, None, None], [None, None, None]]),
      ([[None, None, None]], 
       (0, 2), 'Crosses', 
       [[None, None, 'Crosses']]),
  ]      
)
def test__fill_cell_in_game_board__is_valid(
    game_board_list, player_coord_tuple, 
    player_role, 
    expected_result
    ):
    assert fill_cell_in_game_board(game_board_list, player_coord_tuple, player_role) == expected_result