import pytest
import solution


@pytest.mark.parametrize(
    ("string_input", "string_to_find", "output"),
    (
        ("rkqodlw", "world", True),
        ("cedewaraaossoqqyt", "codewars", True),
        ("katas", "steak", False),
        ("scriptjava", "javascript", True),
        ("scriptingjava", "javascript", True),
    ),
)
def test_solution(string_input, string_to_find, output):
    assert solution.scramble(string_input, string_to_find) == output
