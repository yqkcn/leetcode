from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m, n = len(board), len(board[0])
        # dq[i][j] = [3, 2] 第一个数表示最大得分数，第二个数表示路径数
        dq = []
        for i in range(m):
            cur = []
            for j in range(n):
                cur.append([0, 0])
            dq.append(cur)
        # 初始化右侧边
        for i in range(m - 2, -1, -1):
            if board[i][n - 1] == "X":
                break
            dq[i][n - 1] = [dq[i + 1][n - 1][0] + int(board[i][n - 1]), 1]
        # 初始化底边
        for i in range(n - 2, -1, -1):
            if board[m - 1][i] == "X":
                break
            dq[m - 1][i] = [dq[m - 1][i + 1][0] + int(board[m - 1][i]), 1]
        dq[-1][-1] = [0, 1]
        # 遍历填充动规列表
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == "X" or board[i][j] == "S":
                    continue
                # 上一步为右侧，下侧，右下
                max_num, step_num = 0, 0
                for a, b in [(i + 1, j), (i, j + 1), (i + 1, j + 1)]:
                    if a < 0 or a >= m or b < 0 or b >= n:
                        continue
                    if board[a][b] == "X":
                        continue
                    num1, num2 = dq[a][b]
                    if num1 > max_num:
                        max_num, step_num = num1, num2
                    elif num1 == max_num:
                        step_num += num2
                if board[i][j] != "E":
                    max_num += int(board[i][j])
                if step_num == 0:
                    max_num = 0
                dq[i][j] = [max_num, step_num]
        return dq[0][0]


if __name__ == '__main__':
    s = Solution()
    for case in [
        ["E23", "2X2", "12S"],
        ["E12", "1X1", "21S"],
        ["E11", "XXX", "11S"],
        ["E1156", "XXXX7", "11934", "12345", "8765S"],
    ]:
        print(s.pathsWithMaxScore(case))
