import solution
import pytest


@pytest.mark.parametrize(
    ("input", "output"),
    (
        ([1, 2, 3, 4, 5], [2, 3, 4, 5]),
        ([5, 3, 2, 1, 4], [5, 3, 2, 4]),
        ([2, 2, 1, 2, 1], [2, 2, 2, 1]),
    ),
)
def test_solution(input, output):
    assert solution.remove_smallest(input) == output
