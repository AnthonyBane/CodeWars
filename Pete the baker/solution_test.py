import solution
import pytest

@pytest.mark.parametrize(
    ("recipe", "available", "output"),
    (
        ({"flour": 500, "sugar": 200, "eggs": 1},
         {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
         2
        ),
        (
         {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
         {"sugar": 500, "flour": 2000, "milk": 2000},
         0   
        )
    )
)
def test_solution(recipe, available, output):
    assert solution.cakes(recipe, available) == output