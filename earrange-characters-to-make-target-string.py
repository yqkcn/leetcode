class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        if any(x for x in target if x not in s):
            return 0
        c1, c2 = collections.Counter(s), collections.Counter(target)
        return min(c1[k] // c2[k] for k, v in c2.items())