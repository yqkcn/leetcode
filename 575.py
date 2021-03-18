class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        length = len(candyType)
        set_length = len(set(candyType))
        if set_length >= length // 2:
            return length // 2
        return set_length
