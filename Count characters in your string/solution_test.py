import pytest
import solution


@pytest.mark.parametrize(
    ("input", "output"),
    (("aba", {"a": 2, "b": 1}), ("", {}), ("aa", {"a": 2}), ("aabb", {"b": 2, "a": 2})),
)
def test_solution(input, output):
    assert solution.count(input) == output


@pytest.mark.parametrize(
    ("input", "output"),
    (("aba", {"a": 2, "b": 1}), ("", {}), ("aa", {"a": 2}), ("aabb", {"b": 2, "a": 2})),
)
def test_solution_v2(input, output):
    assert solution.count_v2(input) == output
