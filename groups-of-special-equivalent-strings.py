from typing import List


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        _set = set()
        for word in words:
            key = sorted(word[i] for i in range(len(word)) if i % 2 == 0) + sorted(
                word[i] for i in range(len(word)) if i % 2 != 0)
            _set.add(":".join(key))
        return len(_set)
