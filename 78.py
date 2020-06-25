from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res.extend([_ + [num] for _ in res])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))