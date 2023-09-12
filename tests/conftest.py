from handler import plot_functions
import pytest

@pytest.fixture
def test_math_functions():

    return plot_functions(
        file_path1="data/aerodata.csv",
        file_path2="data/aerodata2.csv"
    )
