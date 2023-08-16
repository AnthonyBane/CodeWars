import pytest
import solution

@pytest.mark.parametrize(
    ("a1", "a2", "output"),
    (
        (
            ["arp", "live", "strong"],
            ["lively", "alive", "harp", "sharp", "armstrong"],
            ["arp", "live", "strong"]
        ),
        (
            ["tarp", "mice", "bull"],
            ["lively", "alive", "harp", "sharp", "armstrong"],
            []
        )
    )
)

def test_solution(a1,a2,output):
    assert solution.in_array(a1,a2) == output