class Solution:
    def isThree(self, n: int) -> bool:
        _set = set()
        for i in range(1, n + 1):
            if not n % i:
                _set.add(i)
        return len(_set) == 3
