from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()

        def dfs(l: int, r: int, char: str):
            if l < 0 or r < 0 or l > r:
                return
            if l == 0 and r == 1:
                char += ")"
                if char not in res:
                    res.add(char)
                return
            dfs(l - 1, r, char + "(")
            dfs(l, r - 1, char + ")")

        dfs(n, n, "")
        return list(res)


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
