import pytest
import solution


@pytest.mark.parametrize(
    ("input", "output"),
    (
        (1, "1.00"),
        (2, "1.25"),
        (3, "1.39"),
        (4, "1.49"),
        (5, "1.57"),
    ),
)
def test_solution(input, output):
    assert solution.series_sum(input) == output
