import solution
import pytest


@pytest.mark.parametrize(
    ("input", "output"), (([], []), (["a", "b", "c"], ["1: a", "2: b", "3: c"]))
)
def test_solution(input, output):
    assert solution.number(input) == output
