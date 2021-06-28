import bisect


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.length = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)
        self.length += 1

    def findMedian(self) -> float:
        a, b = self.length // 2, self.length % 2
        if b:
            return self.nums[a]
        return (self.nums[a] + self.nums[a - 1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
