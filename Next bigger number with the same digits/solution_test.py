import pytest
import solution


@pytest.mark.parametrize(
    ("input", "output"),
    (
        (12, 21),
        (21, -1),
        (513, 531),
        (2017, 2071),
        (414, 441),
        (144, 414)
    )
)
def test_solution(input, output):
    assert solution.next_bigger(input) == output