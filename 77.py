from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < k:
            return []
        if n == k:
            return [list(range(1, n + 1))]
        _max = n - k + 2
        res = [[i] for i in range(1, _max)]
        for i in range(1, k):
            _res = []
            for nums in res:
                for j in range(nums[-1] + 1, _max + i):
                    _res.append(nums + [j])
            res = _res
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combine(5, 2))
