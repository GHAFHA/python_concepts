import pytest


def test_clean_data(test_math_functions):
    cleaned_frame = test_math_functions.clean_data()


def test_calculate_ride_height_combinations(test_math_functions):
    front_height, rear_height = test_math_functions.calculate_ride_height_combinations()
    assert(front_height, int)
    assert(rear_height, int)
