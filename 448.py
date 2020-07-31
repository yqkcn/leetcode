class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        _set = set(nums)
        return [x for x in range(1, len(nums)+1) if x not in _set]