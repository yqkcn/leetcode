def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
    if len(s) == 1:
        return 1

    _max = 0
    l, r = 0, 1
    while r < len(s):
        curr = s[l: r]
        if s[r] not in curr:
            r += 1
            _max = max(_max, len(curr) + 1)
            continue
        if s[r] in curr:
            l += curr.index(s[r]) + 1
            _max = max(_max, len(curr))
            continue
    return _max


if __name__ == '__main__':
    cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
    ]
    for case in cases:
        print(lengthOfLongestSubstring(case))
