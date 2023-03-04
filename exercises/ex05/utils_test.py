"""Test utils functions to see if they are correct."""
__author__ = "730412085"


from exercises.ex05.utils import only_evens, concat, sub


def test_empty() -> None:
    """Test using only_evens and an empty list, results in empty list."""
    test_list = list()
    assert only_evens(test_list) == []


def test_one_odd_element() -> None:
    """Test using only_evens and an odd list, results in empty list."""
    test_list = [7]
    assert only_evens(test_list) == list()


def test_one_even_element() -> None:
    """Test using only_evens and one even element list, results in list with even number."""
    test_list = [4]
    assert only_evens(test_list) == [4]


def test_negative_elements() -> None:
    """Test using only_evens and a list with odd and even positive and negative numbers, results in a list with both positive and negative even numbers in list."""
    test_list = [-1, -2, 4]
    assert only_evens(test_list) == [-2, 4]


def test_both_empty() -> None:
    """Test using concat and two empty lists, results in empty list."""
    test_a: list[int] = list()
    test_b: list[int] = list()
    assert concat(test_a, test_b) == list()


def test_list_a_empty() -> None:
    """Test using concat and one empty list and one filled list, results in list with numbers from filled list."""
    test_a = list()
    test_b = [1, 2, 3, 4]
    assert concat(test_a, test_b) == [1, 2, 3, 4]


def test_list_b_empty() -> None:
    """Test using concat and one empty list and one filled list, results in list with numbers from filled list."""
    test_a = [1, 4, 5, 6]
    test_b = list()
    assert concat(test_a, test_b) == [1, 4, 5, 6]


def test_list_a_empty_and_one() -> None:
    """Test using concat and one empty list and one filled list, results in list with number from filled list."""
    test_a = list()
    test_b = [1]
    assert concat(test_a, test_b) == [1]


def test_list_b_empty_and_one() -> None:
    """Test using concat and one empty list and one filled list, results in list with number from filled list."""
    test_a = [1]
    test_b = list()
    assert concat(test_a, test_b) == [1]


def test_normal_use() -> None:
    """Test using concat and two unique, same lengthlists, results in one list with all values."""
    test_a = [1, 3, 4, 5]
    test_b = [2, 7, 9, 8]
    assert concat(test_a, test_b) == [1, 3, 4, 5, 2, 7, 9, 8]


def test_normal_use_identical() -> None:
    """Test using concat and two identical lists, results in one list with all values."""
    test_a = [1, 3, 4, 5]
    test_b = [1, 3, 4, 5]
    assert concat(test_a, test_b) == [1, 3, 4, 5, 1, 3, 4, 5]


def test_normal_use_dif_legths() -> None:
    """Test using concat and two different lengthedlists, results in one list with all values."""
    test_a = [1, 3, 4, 5, 6]
    test_b = [2, 7, 9, 8]
    assert concat(test_a, test_b) == [1, 3, 4, 5, 6, 2, 7, 9, 8]


def test_empty_sub() -> None:
    """Test using sub and one empty list, start_idx = 0, and end_idx = 0, results in empty list."""
    test_list = list()
    test_start = 0
    test_end = 0
    assert sub(test_list, test_start, test_end) == []


def test_st_idx_zero() -> None:
    """Test using sub and one filled list and start_idx = 0 and test_idx = some number, results in filled list."""
    test_list = [1, 2, 3, 4]
    test_start = 0
    test_end = 3
    assert sub(test_list, test_start, test_end) == [1, 2, 3, 4]


def test_end_idx_zero() -> None:
    """Test using sub and one filled list and start_idx = 0 and end_idx = 0, results in list with one number."""
    test_list = [1, 2, 3, 4]
    test_start = 0
    test_end = 0
    assert sub(test_list, test_start, test_end) == [1]


def test_start_idx_negative() -> None:
    """Test using sub and one filled list and start_idx = negative number and end_idx = some number, results in filled list."""
    test_list = [1, 2, 3, 4]
    test_start = -2
    test_end = 2
    assert sub(test_list, test_start, test_end) == [1, 2, 3]


def test_end_idx_large() -> None:
    """Test using sub and filled list and start_idx = 0 and end_idx = some number, results in filled list."""
    test_list = [1, 2, 3, 4]
    test_start = 0
    test_end = 7
    assert sub(test_list, test_start, test_end) == [1, 2, 3, 4]


def test_end_idx_negative() -> None:
    """Test using sub and filled list and start_idx = 0 and end_idx = negative number."""
    test_list = [1, 2, 3, 4]
    test_start = 0
    test_end = -2
    assert sub(test_list, test_start, test_end) == [1, 2, 3]


def test_start_idx_same_as_list_length() -> None:
    """Test using sub and filled list and start_idx = length of list and end_idx = some number, results in filled list."""
    test_list = [1, 2, 3, 4]
    test_start = len(test_list)
    test_end = 3
    assert sub(test_list, test_start, test_end) == list()