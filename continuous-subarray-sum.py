from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        _map = {0:-1}
        for i, num in enumerate(nums):
            total += num
            remainder = total % k
            if remainder in _map:
                if i - _map[remainder] >= 2:
                    return True 
            else:
                _map[remainder] = i
        return False