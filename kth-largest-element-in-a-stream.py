from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        for i, num in enumerate(self.nums):
            if val >= num:
                self.nums.insert(i, val)
                break
        if not self.nums or val < self.nums[-1]:
            self.nums.append(val)
        return self.nums[self.k - 1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
