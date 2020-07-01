class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = 0
        while True:
            _num = 2 ** num
            if _num == n:
                return True
            if _num > n:
                return False
            num += 1