import pytest

from solution import decode


@pytest.mark.parametrize(
    "s, result",
    (
        ("1273409kuqhkoynvvknsdwljantzkpnmfgf", "uogbucwnddunktsjfanzlurnyxmx"),
        ("761328qockcouoqmoayqwmkkic", "Impossible to decode"),
        ("1544749cdcizljymhdmvvypyjamowl", "mfmwhbpoudfujjozopaugcb"),
        ("1122305vvkhrrcsyfkvejxjfvafzwpsdqgp", "rrsxppowmjsrclfljrajtybwviqb"),
    ),
)
def test(s, result):
    assert decode(s) == result
