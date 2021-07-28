class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def _is_ok(_s: str) -> bool:
            _s = set(_s)
            for i in _s:
                if i.lower() not in _s or i.upper() not in _s:
                    return False
            return True

        ans = ""
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 <= len(ans) or not _is_ok(s[i:j + 1]):
                    continue
                ans = s[i:j + 1]
        return ans
