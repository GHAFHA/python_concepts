import pytest


def test_clean_data(test_math_functions):
    test_math_functions.clean_data()


def test_calculate_ride_height_combinations(test_math_functions):
    test_math_functions.display_ride_height_combinations()


def test_ride_height_combinations(test_math_functions):
    j = 0
    chassis_heave, chassis_angle, front_ride_height, rear_ride_height = test_math_functions.calculate_ride_height_combinations(j)
    assert isinstance(chassis_heave, float)
    assert isinstance(chassis_angle, float)
    assert isinstance(front_ride_height, float)
    assert isinstance(rear_ride_height, float)


def test_ride_height_diff(test_math_functions):
    difference = test_math_functions.calc_ride_height_difference()
    assert isinstance(difference, float)

def test_calculate_min_max_mean(test_math_functions):
    difference = test_math_functions.calculate_min_max_mean()

def test_plot_rear_front_ride_height_vs_cla(test_math_functions):
    difference = test_math_functions.plot_rear_front_ride_height_vs_cla()