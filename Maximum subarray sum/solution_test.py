import pytest
import solution

@pytest.mark.parametrize(("input", "result"),
                         (
                             ([], 0),
                             ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
                             ([-2, -1, -3, -4, -1, -2, -1, -5, -4], 0),
                             ([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43], 155)
                         )
)
def test_solution(input, result):
    assert solution.max_sequence(input) == result
