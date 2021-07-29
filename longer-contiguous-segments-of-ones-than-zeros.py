class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        return max(len(x) for x in s.split("0")) > max(len(x) for x in s.split("1"))
