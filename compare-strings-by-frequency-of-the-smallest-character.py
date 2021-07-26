import bisect
from collections import Counter
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(w: str) -> int:
            counter = Counter(w)
            return counter[min(counter.keys())]

        queries = [f(q) for q in queries]
        words = [f(w) for w in words]
        words = sorted(words)
        length = len(words)
        return [length - bisect.bisect_right(words, q) for q in queries]
