class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []

    def addNum(self, num: int) -> None:
        import bisect
        bisect.insort(self.values, num)

    def findMedian(self) -> float:
        length = len(self.values)
        if length % 2 == 0:
            idx1, idx2 = length // 2, length // 2 - 1
            return (self.values[idx1] + self.values[idx2]) / 2
        return self.values[(length - 1) // 2]
