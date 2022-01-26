import collections
from typing import List


class DetectSquares:

    def __init__(self):
        # 统计点的个数
        self.counter = collections.Counter()
        # 记录 x 对应的 y
        self.xs = collections.defaultdict(set)

    def add(self, point: List[int]) -> None:
        # 点的个数加 1
        self.counter[tuple(point)] += 1
        # 记录 x 和 y 关系
        self.xs[point[0]].add(point[1])

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
        for a in self.xs[x]:
            if y == a:
                continue
            side = abs(a - y)
            res += self.counter[(x, a)] * self.counter[(x + side, y)] * self.counter[(x + side, a)]
            res += self.counter[(x, a)] * self.counter[(x - side, y)] * self.counter[(x - side, a)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
