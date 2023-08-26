import pytest


def test_clean_data(test_math_functions):
    cleaned_frame = test_math_functions.clean_data()
    assert cleaned_frame