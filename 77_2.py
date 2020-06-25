class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [[]]
        for i in range(1, n + 1):
            res.extend([_ + [i] for _ in res])
        return [_ for _ in res if len(_) == k]