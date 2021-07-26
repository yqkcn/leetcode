class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = ""
        while a or b:
            if a == 0:
                res += "b" * b
                break
            if b == 0:
                res += "a" * a
                break
            if a == b:
                _s = "ba" if res.endswith("aa") else "ab"
                res += _s * a
                break
            if a > b:
                _s = "aab" if not res.endswith("a") else "baa"
                res += _s
                a -= 2
                b -= 1
                continue
            if a < b:
                _s = "bba" if not res.endswith("b") else "abb"
                res += _s
                b -= 2
                a -= 1
                continue
        return res
