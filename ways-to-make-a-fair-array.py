class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        res = 0
        a, b, c, d = 0, sum(nums[::2]), 0, sum(nums[1::2])
        for i, g in enumerate(nums):
            if i % 2 == 0:
                b -= g
                if a + d == c + b:
                    res += 1
                a += g
            else:
                d -= g
                if a + d == c + b:
                    res += 1
                c += g
        return res
