class Solution:
    def countBits(self, num: int) -> List[int]:
        return [f"{_:b}".count("1") for _ in range(num+1)]