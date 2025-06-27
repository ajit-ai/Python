import pytest
from sorting import merge_sort

# Basic test cases
def test_sorted_input():
    assert merge_sort([1, 2, 3]) == [1, 2, 3], "Failed on sorted input"

def test_reverse_sorted_input():
    assert merge_sort([3, 2, 1]) == [1, 2, 3], "Failed on reverse-sorted input"

def test_unsorted_input():
    assert merge_sort([97, 122, 109]) == [97, 109, 122], "Failed on unsorted input"

def test_empty_list():
    assert merge_sort([]) == [], "Failed on empty list"

def test_single_element():
    assert merge_sort([42]) == [42], "Failed on single element"

# Fixture for reusable test data
@pytest.fixture
def sample_list():
    return [5, 2, 8, 1, 9]

def test_sample_list(sample_list):
    assert merge_sort(sample_list) == [1, 2, 5, 8, 9], "Failed on sample list"

# Parameterized test for multiple inputs
@pytest.mark.parametrize("input_list, expected", [
    ([1, 1, 1], [1, 1, 1]),  # Duplicates
    ([100, 50, 75], [50, 75, 100]),  # Unsorted
    ([-1, -3, -2], [-3, -2, -1]),  # Negative numbers
])
def test_parameterized(input_list, expected):
    assert merge_sort(input_list) == expected, f"Failed on input {input_list}"

# Test for expected exception (e.g., invalid input)
def test_invalid_input():
    with pytest.raises(TypeError):
        merge_sort([1, "2", 3])  # Mixed types should raise TypeError