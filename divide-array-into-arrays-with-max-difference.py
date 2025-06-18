from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        # 从前往后遍历，一次取三个，这三个数字理论上就是距离最近的，满足 k 限制即可
        res = []
        idx = 0
        while idx < len(nums):
            a, b, c = nums[idx], nums[idx+1], nums[idx+2]
            if b-a <= k and c-b <= k and c-a <= k:
                res.append([a, b, c])
                idx += 3
            else:
                return []
        return res



if __name__ == '__main__':
    import itertools
    print(list(itertools.permutations("abcdef", 3)))