class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = list(sorted(set(arr)))
        nums = {num:i+1 for i, num in enumerate(nums)}
        return [nums[_] for _ in arr]