class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        f_str = f"{n:2b}"
        for i in range(len(f_str) - 1):
            if f_str[i] == f_str[i + 1]:
                return False
        return True
