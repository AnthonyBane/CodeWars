import pytest
import solution


@pytest.mark.parametrize(
    ("product", "output"), ((4895, [55, 89, True]), (5895, [89, 144, False]))
)
def test_solution(product, output):
    assert solution.productFib(product) == output
