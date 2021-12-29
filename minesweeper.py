from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])

        def dfs(x, y, m, n):
            if not (0 <= x < m and 0 <= y < n):
                return
            # 已挖出
            if board[x][y] != "E":
                return
            ns = self.get_ns(x, y, m, n)
            num = sum([1 if board[i][j] == "M" else 0 for i, j in ns])
            # 周围无地雷
            if not num:
                board[x][y] = "B"
                # 找邻居
                for i, j in ns:
                    dfs(i, j, m, n)
            else:
                board[x][y] = str(num)

        r, c = click
        # 挖到地雷
        if board[r][c] == "M":
            board[r][c] = "X"
            return board
        if board[r][c] == "E":
            dfs(r, c, m, n)
        return board

    def get_ns(self, r, c, m, n):
        ans = []
        for i, j in [
            (r - 1, c - 1),
            (r - 1, c),
            (r - 1, c + 1),
            (r, c - 1),
            (r, c + 1),
            (r + 1, c - 1),
            (r + 1, c),
            (r + 1, c + 1)
        ]:
            if 0 <= i < m and 0 <= j < n:
                ans.append((i, j))
        return ans
