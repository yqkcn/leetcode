class Solution:
    def countArrangement(self, n: int) -> int:
        num = 0
        def dfs(vis:set):
            nonlocal num

            if len(vis) == n:
                num += 1
                return
            idx = len(vis) + 1
            for i in range(1, n+1):
                if i in vis:
                    continue
                if not i % idx or not idx % i:
                    vis.add(i)
                    dfs(vis)
                    vis.remove(i)
        dfs(set())
        return num