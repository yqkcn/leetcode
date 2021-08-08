from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        _s = ""
        for word in words:
            _s += word
            if _s == s:
                return True
        return False