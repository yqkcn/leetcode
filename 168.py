class Solution:
    def convertToTitle(self, n: int) -> str:
        import string
        b = {i: k for i, k in enumerate(string.ascii_uppercase)}
        res = ""
        while n > 0:
            n -= 1
            num = n % 26
            res = b[num] + res
            n = n // 26
        if n:
            res = b[n] + res
        return res
