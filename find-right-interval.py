from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        cache = {}
        for i, (a, b) in enumerate(intervals):
            cache[a] = i
        starts = sorted(cache.keys())
        result = []
        for a, b in intervals:
            if starts[-1] < b:
                result.append(-1)
                continue
            # 去 starts 里找大于b的最小的
            m, n = 0, len(starts)-1
            while m < n:
                c = (m+n)//2
                # 满足
                if starts[c] >= b:
                    n = c
                else:
                    m = c + 1
            # n 是结果
            result.append(cache[starts[n]])
        return result


if __name__ == '__main__':
    a = Solution().findRightInterval([[1,4],[2,3],[3,4]])
    print(a)

