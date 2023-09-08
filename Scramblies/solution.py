from collections import Counter


def scramble(s1, s2):
    s1_dict = Counter(s1)
    s2_dict = Counter(s2)

    return all(
        (s2_key in s1_dict) and (s2_count <= s1_dict[s2_key])
        for s2_key, s2_count in s2_dict.items()
    )
