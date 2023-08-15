import solution
import pytest

@pytest.mark.parametrize(
    ("inputs", "result"),
    (
        ((2, 0.5, 1), 1),
        ((3, 0.66, 1.5), 3),
        ((30, 0.66, 1.5), 15),
        ((30, 0.75, 1.5), 21)
    )
)

def test_solution(inputs, result):
    h,bounce,window = inputs
    assert solution.bouncing_ball(h,bounce,window) == result
