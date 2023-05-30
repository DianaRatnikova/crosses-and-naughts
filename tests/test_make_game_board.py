from functions.game_board import make_game_board


def test__make_game_board():
    assert make_game_board() == [[None, None, None], [None, None, None], [None, None, None]]