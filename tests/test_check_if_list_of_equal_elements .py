
from functions.victory import check_if_list_of_equal_elements
import pytest


@pytest.mark.parametrize(
  "list_to_check, expected_result",
  [
    ([None, None, None], True),
    (['wverfd', None, None], False),
    ([None], True),
    (['d'], True),
    ([], False),
  ]      
)
def test__check_if_list_of_equal_elements__is_valid(list_to_check, expected_result):
    assert check_if_list_of_equal_elements(list_to_check) is expected_result


@pytest.mark.parametrize(
  "list_to_check, expected_error",
  [
    (None, TypeError),
    (3654, TypeError),
  ]      
)
def test__check_if_list_of_equal_elements__errors(list_to_check, expected_error):
    with pytest.raises(expected_error):
        check_if_list_of_equal_elements(list_to_check)
