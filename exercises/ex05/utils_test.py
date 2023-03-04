"""Test utils functions to see if they are correct."""
__author__ = "730412085"


from exercises.ex05.utils import only_evens, concat, sub
"""Utils tests for only_evens."""
def test_empty() -> None:
    assert only_evens([]) == []

def test_one_odd_element() -> None:
    test_list: list[int] = [7]
    only_evens(test_list) == []

def test_one_even_element() -> None:
    test_list: list[int] = [4]
    only_evens(test_list) == [4]

def test_negative_elements() -> None:
    test_list: list[int] = [-1,-2,4]
    only_evens(test_list) == [-2,4]


"""Utils tests for concat."""
def test_both_empty() -> None:
    test_a = []
    test_b = []
    concat(test_a, test_b) == []

def test_list_a_empty() -> None:
    test_a = []
    test_b = [1,2,3,4]
    concat(test_a, test_b) == [1,2,3,4]

def test_list_b_empty() -> None:
    test_a = [1,4,5,6]
    test_b = []
    concat(test_a, test_b) == [1,4,5,6]

def test_normal_use() -> None:
    test_a = [1,3,4,5,6]
    test_b = [1,2,3,4]
    concat(test_a, test_b) == [1,3,4,5,6,1,2,3,4]


"""Utils tests for sub."""
def test_empty() -> None:
    test_list = []
    test_start = 0
    test_end = 0
    sub(test_list, test_start, test_end) == []

def test_st_idx_zero() -> None:
    test_list = [1,2,3,4]
    test_start = 0
    test_end = 3
    sub(test_list, test_start, test_end) == [1,2,3,4]

def test_end_idx_zero() -> None:
    test_list = [1,2,3,4]
    test_start = 0
    test_end = 0
    sub(test_list, test_start, test_end) == [1]

def test_start_idx_negative() -> None:
    test_list = [1,2,3,4]
    test_start = -2
    test_end = 2
    sub(test_list, test_start, test_end) == [1,2,3]

def test_end_idx_large() -> None:
    test_list = [1,2,3,4]
    test_start = 0
    test_end = 7
    sub(test_list, test_start, test_end) == [1,2,3,4]

def test_end_idx_negative() -> None:
    test_list = [1,2,3,4]
    test_start = 0
    test_end = -2
    sub(test_list, test_start, test_end) == [1,2,3,4]