class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        return [x for x in nums if x%2] + [x for x in nums if not x%2]