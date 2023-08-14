import pytest
import solution

@pytest.mark.parametrize(("input", "output"),
                         (
                            (
                                (
                                [121, 144, 19, 161, 19, 144, 19, 11],
                                [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
                                ),
                                True
                            ),
                            (
                                (
                                [121, 144, 19, 161, 19, 144, 19, 11],
                                [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]),
                                False
                            ),
                            (
                                (
                                [121, 144, 19, 161, 19, 144, 19, 11],
                                [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
                                ),
                                False
                            )
                         )
)

def test_solution(input, output):
    array1, array2 = input
    assert solution.comp(array1,array2) == output