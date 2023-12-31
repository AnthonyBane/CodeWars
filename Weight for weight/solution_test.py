import pytest
import solution


@pytest.mark.parametrize(
    ("input", "output"),
    ( 
     ("103 123 4444 99 2000", "2000 103 123 4444 99"),
     ("2000 10003 1234000 44444444 9999 11 11 22 123", "11 11 2000 10003 22 123 1234000 44444444 9999"),
     ("","")
    )
)
def test_solution(input, output):
    assert solution.order_weight(input) == output