import solution
import pytest


@pytest.mark.parametrize(
    ("inputs", "output"),
    (
        (([], 1), 0),
        (([5], 1), 5),
        (([2], 5), 2),
        (([1, 2, 3, 4, 5], 1), 15),
        (([1, 2, 3, 4, 5], 100), 5),
        (([2, 2, 3, 3, 4, 4], 2), 9),
    ),
)
def test_solution(inputs: (list, int), output: int):
    customers, tills = inputs
    assert solution.queue_time(customers, tills) == output
