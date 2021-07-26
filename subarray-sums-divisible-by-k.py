from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        import collections

        counter = collections.defaultdict(int)
        _sum = 0
        for num in nums:
            _sum += num
            counter[_sum % k] += 1
        res = 0
        for _k, _v in counter.items():
            if _k == 0:
                res += _v
            res += _v * (_v - 1) // 2
        return res

if __name__ == '__main__':
    Solution().subarraysDivByK([4,5,0,-2,-3,1], 5)