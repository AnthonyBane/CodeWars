import pytest
import solution


@pytest.mark.parametrize(
    ("input_a", "input_b", "output"),
    (
        (1, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (1, 100, [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]),
        (10, 89, [89]),
        (10, 100, [89]),
        (90, 100, []),
        (89, 135, [89, 135]),
    ),
)
def test_solution(input_a, input_b, output):
    assert solution.sum_dig_pow(input_a, input_b) == output
