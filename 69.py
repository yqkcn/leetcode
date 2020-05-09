def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    l = 0
    r = x // 2 + 1
    while l < r:
        m = (l + r + 1) >> 1
        s = m * m
        if s > x:
            r = m - 1
        else:
            l = m
    return l


if __name__ == '__main__':
    test_cases = [
        (3, 1),
        (4, 2),
        (8, 2),
        (15, 3),
        (81, 9),
    ]
    for case, expected in test_cases:
        assert mySqrt(case) == expected
