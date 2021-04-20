class Solution:
    def countLargestGroup(self, n: int) -> int:
        import collections

        res = collections.defaultdict(int)
        for i in range(1, n + 1):
            cur = sum(int(i) for i in str(i))
            res[cur] += 1
        target = max(res.values())
        return len([1 for v in res.values() if v == target])
