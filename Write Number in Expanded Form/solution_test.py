import solution
import pytest


@pytest.mark.parametrize(
    ('input', 'output'),
    (
        (12, '10 + 2'),
        (42, '40 + 2'),
        (70304, '70000 + 300 + 4')
    )
)

def test_solution(input, output):
    assert solution.expanded_form(input) == output