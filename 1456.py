def maxVowels(s: str, k: int) -> int:
    if not s or not k:
        return 0
    _processed = set()

    def _count(_chars):
        _n = 0
        for _c in _chars:
            if _c in ['a', 'e', 'i', 'o', 'u']:
                _n += 1
        _processed.add(_chars)
        return _n

    _res = 0
    for i in range(0, len(s)):
        _str = s[i: i + k]
        if _str in _processed:
            continue
        _res = max(_res, _count(_str))
    return _res


if __name__ == '__main__':
    for case in [
        ('abciiidef', 3),
        ('aeiou', 2),
        ('leetcode', 3),
        ('rhythms', 4),
        ('tryhard', 4),
        ("weallloveyou", 7)
    ]:
        print(maxVowels(*case))
