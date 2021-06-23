import bisect
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        length = len(nums)
        idx = k
        window = sorted(nums[:idx])
        res = []
        a, b = k // 2, k % 2
        while True:
            # 偶数
            if b == 0:
                res.append((window[a] + window[a - 1]) / 2)
            else:
                res.append(window[a])
            if idx >= length:
                break
            # 右移
            window.remove(nums[idx - k])
            bisect.insort(window, nums[idx])
            idx += 1
        return res
