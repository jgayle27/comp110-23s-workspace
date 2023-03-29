"""Ex07 - Testing Dictionary Functions."""

__author__ = "730412085"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_normal_use_invert() -> None:
    """Test using invert and a dictionary of several strs, results in dictionary with values as the keys and the keys as values."""
    test_dictionary = {"a": "!", "b": "*", "c": "3", "d": "()"}
    assert invert(test_dictionary) == {"!": "a", "*": "b", "3": "c", "()": "d"}


def test_normal_use_with_small_dictionary() -> None:
    """Test using invert and a dictionary where the values are duplicates so the result would have duplicate key values, results in KeyError."""
    test_dictionary = {"cat": "fish"}
    assert invert(test_dictionary) == {"fish": "cat"}


def test_empty_dict() -> None:
    """Test using invert and an empty dictionary, results in ."""
    test_dictionary = {}
    assert invert(test_dictionary) == {}


# def test_normal_use_with_identical_keys() -> None:
#    """Test using invert and a dictionary where the values are duplicates so the result would have duplicate key values, results in KeyError."""
#    test_dictionary = {"a":"!", "b":"*", "c":"3", "d":"!"}
#    assert invert(test_dictionary) == KeyError("cannot have two identical keys!")


def test_normal_use_color() -> None:
    """Tests favorite_color using a normal sized dictionary with a duplicate of one value, results in a str of that value."""
    test_color_dict = {"Felicia": "green", "Skippy": "purple", "Toulouse": "blue", "Max": "blue"}
    assert favorite_color(test_color_dict) == "blue"


def test_normal_use_with_unique_values() -> None:
    """Tests favorite_color using a normal sized dictionary with an equal amount of values, results in the first value as a str."""
    test_color_dict = {"Felicia": "green", "Skippy": "purple", "Toulouse": "blue", "Max": "red"}
    assert favorite_color(test_color_dict) == "green"


def test_empty_dictionary() -> None:
    """Tests favorite_color using empty dictionary, results in empty dictionary."""
    test_color_dict = {}
    assert favorite_color(test_color_dict) == ()


def test_normal_use_count() -> None:
    """Tests count using a normal sized list and duplicates of various values, results in a dictionary with the value as a str and the number of occurences as an int."""
    test_count_list = ("cat", "dog", "fish", "cat", "fish")
    assert count(test_count_list) == {"cat": 2, "dog": 1, "fish": 2}


def test_normal_use_with_unique_list() -> None:
    """Tests count using a list with completely unique variables, results in a dictionary where every key has the value of 1."""
    test_count_list = ("cat", "dog", "fish")
    assert count(test_count_list) == {"cat": 1, "dog": 1, "fish": 1}


def test_count_with_empty_list() -> None:
    """Tests count using an empty list, results in an empty dictionary."""
    test_count_list = ()
    assert count(test_count_list) == {}