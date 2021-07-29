class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        import re
        return len(set(int(x) for x in re.split(r"[a-z]+", word) if x))
