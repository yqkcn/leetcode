from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        left, right = 0, 0
        for _l, _r in intervals:
            if _r < right:
                continue
            if _l > right:
                res.append([_l, _r])
                left, right = _l, _r
                continue
            if not res:
                res.append([_l, _r])
            else:
                res[-1][1] = _r
            right = _r
        return res


if __name__ == '__main__':
    s = Solution()
    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
    ]
    for intervals, expected in test_cases:
        assert s.merge(intervals) == expected
