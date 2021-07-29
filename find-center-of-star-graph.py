from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        _set = set()
        for a, b in edges:
            if a in _set:
                return a
            _set.add(a)
            if b in _set:
                return b
            _set.add(b)
