class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        _dict = {0: -1}
        res = 0
        pre_sum = 0
        for i, num in enumerate(nums):
            if num == 1:
                pre_sum += 1
            else:
                pre_sum -= 1
            if pre_sum in _dict:
                res = max(res, i - _dict[pre_sum])
            else:
                _dict[pre_sum] = i
        return res
