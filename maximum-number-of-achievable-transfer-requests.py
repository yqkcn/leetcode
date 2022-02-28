from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        nums = [0] * n
        ans = 0

        def dfs(total: int, idx: int):
            nonlocal ans

            # total 标示处理的请求数， idx 标示已经处理到的索引数
            # 如果当前满足条件，更新一下结果
            if not any(nums):
                ans = max(ans, total)

            if idx >= len(requests):
                return

            # 选当前节点
            a, b = requests[idx]
            nums[a] -= 1
            nums[b] += 1
            dfs(total + 1, idx + 1)
            # 还原
            nums[a] += 1
            nums[b] -= 1
            # 不选当前节点
            dfs(total, idx + 1)

        dfs(0, 0)
        return ans
