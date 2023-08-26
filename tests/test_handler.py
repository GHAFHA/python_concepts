import pytest

def test_addition(test_math_functions):
    result = test_math_functions.add_integers()
    isinstance(result,int)

def test_substractoin(test_math_functions):
    result = test_math_functions.sub_integers()
    isinstance(result,int)

def test_multiplication(test_math_functions):
    result = test_math_functions.multiply_integers()
    isinstance(result, str)