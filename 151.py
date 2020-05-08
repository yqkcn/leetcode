def reverseWords(s: str) -> str:
    import re

    s = s.strip()
    s = re.sub("\\s\\s+", " ", s)
    return " ".join(reversed(s.split()))


if __name__ == '__main__':
    test_cases = [
        ("the sky is blue", "blue is sky the"),
        ("  hello world!  ", "world! hello"),
        ("a good   example", "example good a")
    ]
    for case, expected in test_cases:
        assert reverseWords(case) == expected
