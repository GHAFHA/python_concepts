from handler import math_functions
import pytest

@pytest.fixture
def test_math_functions():

    return math_functions(
        file_path="data/aerodata.csv"
    )