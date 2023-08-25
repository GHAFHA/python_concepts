import pytest

def test_addition(test_math_functions):
    result = test_math_functions.add_integers()
    isinstance(result,int)
