from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        res = 0
        strs = [(s.count("0"), s.count("1")) for s in strs]

        def dfs(idx, num_0, num_1, length):
            nonlocal res
            if idx >= len(strs):
                return

            # 不取当前值
            dfs(idx + 1, num_0, num_1, length)
            # 取当前值
            num_0 += strs[idx][0]
            num_1 += strs[idx][1]
            length += 1
            if num_0 <= m and num_1 <= n:
                if length > res:
                    res = length
                dfs(idx + 1, num_0, num_1, length)

        dfs(0, 0, 0, 0)
        return res


if __name__ == '__main__':
    print(Solution().findMaxForm(["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], 9, 80))
