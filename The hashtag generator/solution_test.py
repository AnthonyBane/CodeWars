import solution
import pytest

@pytest.mark.parametrize(
    ("input", "output"),
    (
        ('Codewars', '#Codewars'),
        ('Codewars      ', '#Codewars'),
        ('      Codewars', '#Codewars'),
        ('Codewars Is Nice', '#CodewarsIsNice'),
        ('codewars is nice', '#CodewarsIsNice'),
        ('CoDeWaRs is niCe', '#CodewarsIsNice'),
        ('c i n', '#CIN'),
        ('codewars  is  nice', '#CodewarsIsNice'),
        ('', False,),
        ('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat', False)
    )
)

def test_solution(input, output):
    assert solution.generate_hashtag(input) == output