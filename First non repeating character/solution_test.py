import pytest
import solution 

@pytest.mark.parametrize(
    ("input", "output"),
    (
        ('a','a'),
        ('stress','t'),
        ('moonmen','e'),
    )
)
def test_soltuion(input, output):
    assert solution.first_non_repeating_letter(input) == output