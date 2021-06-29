from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        import collections
        counter = collections.Counter("".join(words))
        for k, v in counter.items():
            if v % len(words):
                return False
        return True
