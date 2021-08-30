class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        m, n = len(a), len(b)
        idx = 1
        flag = "0"
        while idx <= m or idx <= n:
            char = flag
            if idx <= m:
                char += a[-1 * idx]
            if idx <= n:
                char += b[-1 * idx]
            num = char.count("1")
            c, d = num // 2, num % 2
            res.append("1" if d else "0")
            flag = "1" if c else "0"
            idx += 1
        if flag == "1":
            res.append("1")
        return "".join(res[::-1])