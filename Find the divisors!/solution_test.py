import pytest
import solution


@pytest.mark.parametrize(
    ("input", "output"),
    (
        (15, [3, 5]),
        (12, [2, 3, 4, 6]),
        (13, "13 is prime"),
    ),
)
def test_divisors(input, output):
    assert solution.divisors(input) == output
