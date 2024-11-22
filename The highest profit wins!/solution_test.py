import pytest
import solution


@pytest.mark.parametrize(
    ("input", "output"), (([1, 2, 3, 4, 5], [1, 5]), ([2334454, 5], [5, 2334454]))
)
def test_solution(input, output):
    assert solution.min_max(input) == output
