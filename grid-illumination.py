from typing import List


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 五个计数器，分别统计灯泡数，行数，列数，对角线1数和对角线2数
        import collections
        lamp1 = collections.defaultdict(int)
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)
        diagonal1 = collections.defaultdict(int)
        diagonal2 = collections.defaultdict(int)
        # 遍历起始灯泡
        for r, c in lamps:
            lamp1[(r, c)] += 1
            rows[r] += 1
            cols[c] += 1
            diagonal1[c - r] += 1
            diagonal2[r + c] += 1
        ans = []
        for r, c in queries:
            # 判断是否被照亮
            if lamp1.get((r, c)) or rows.get(r) or cols.get(c) or diagonal1.get(c - r) or diagonal2.get(r + c):
                ans.append(1)
            else:
                ans.append(0)
            # 关闭当前位置和邻居位置的灯
            for a in [-1, 0, 1]:
                for b in [-1, 0, 1]:
                    e, f = r + a, c + b
                    # 无效的下标
                    if not (0 <= e < n) or not (0 <= f < n):
                        continue
                    # 位置未亮
                    if not lamp1.get((e, f)):
                        continue
                    # 关闭灯
                    num = lamp1.pop((e, f))
                    # 对应的行，列，对角线减一
                    rows[e] -= num
                    cols[f] -= num
                    diagonal1[f - e] -= num
                    diagonal2[e + f] -= num
        return ans


if __name__ == '__main__':
    Solution().gridIllumination(6, [[2, 5], [4, 2], [0, 3], [0, 5], [1, 4], [4, 2], [3, 3], [1, 0]],
                                [[4, 3], [3, 1], [5, 3], [0, 5], [4, 4], [3, 3]])
