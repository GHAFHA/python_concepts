from handler import math_functions
import pytest

@pytest.fixture
def test_math_functions():

    return math_functions(
        integer1=1,
        integer2=1
    )