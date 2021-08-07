class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        import collections
        return len(set(collections.Counter(s).values())) == 1
