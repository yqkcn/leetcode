class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = num1.split("+")
        c, d = num2.split("+")
        a, b, c, d = int(a), int(b[:-1]), int(c), int(d[:-1])
        e = a * c - b * d
        f = a * d + b * c
        return f"{e}+{f}i"
