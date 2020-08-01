class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return list(sorted(_*_ for _ in A))