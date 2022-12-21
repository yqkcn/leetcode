class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        res = 0
        while True:
            a, b, c = sorted([a, b, c])
            # 较大的两个数减 1
            if b and c:
                b, c = b - 1, c - 1
                res += 1
            else:
                break
        return res