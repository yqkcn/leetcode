class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def get_mul(_nums):
            _res = 1
            for _num in _nums:
                _res *= _num
            return _res
        res, cache = [], {}
        for i, num in enumerate(nums):
            if num not in cache:
                cache[num] = get_mul(nums[:i] + nums[i+1:])
            res.append(cache[num])
        return res