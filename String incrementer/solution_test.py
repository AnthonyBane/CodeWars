import pytest
import solution


@pytest.mark.parametrize(
    ("input", "output"),
    (
        ("foo", "foo1"),
        ("foobar23", "foobar24"),
        ("foo0042", "foo0043"),
        ("foo9", "foo10"),
        ("foo099", "foo100"),
    ),
)
def test_solution(input, output):
    assert solution.increment_string(input) == output
