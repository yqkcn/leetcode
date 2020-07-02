class Solution:
    def firstUniqChar(self, s: str) -> int:
        import collections
        counter = collections.defaultdict(int)
        for _s in s:
            counter[_s] += 1
        for i, _s in enumerate(s):
            if counter[_s] == 1:
                return i
        return -1
