from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        import collections

        counter = collections.Counter()
        for i, num in enumerate(nums):
            counter[num - i] += 1
        ans = 0
        cur = sum(v for k, v in counter.items() if k <= 0)
        max_cur = cur
        flag = False
        for k, num in enumerate(nums):
            cur -= counter[-1 * k]
            counter[num - k] -= 1
            # 其他的都减 1，之前差值为 0 的不再满足
            if num < len(nums):
                cur += 1
            # 其他的 key 都加 1
            # counter = {k+1: v for k, v in counter.items()}
            counter[num - len(nums) - k] += 1
            if cur > max_cur:
                max_cur = cur
                ans = k
                flag = True
        return ans + 1 if flag else 0


if __name__ == '__main__':
    print(Solution().bestRotation([1,3,0,2,4,3,4,5,3,11,3,5,2,5,12, 4,9]))
