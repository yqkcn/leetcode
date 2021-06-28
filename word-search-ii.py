from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        # 构造前缀树
        tree = {}
        for word in words:
            node = tree
            for letter in word:
                # 不存在，设为空字典
                node = node.setdefault(letter, {})
            # 保存单词
            node["$"] = word

        result = []

        # 定义搜索函数
        def dfs(r: int, c: int, parent: dict):
            letter = board[r][c]
            cur_node = parent[letter]
            # 判断是否匹配到单词
            # 匹配到直接弹出，防止重复添加
            if word := cur_node.pop("$", None):
                result.append(word)
            # 将当前位置设为 #， 标记已找过
            board[r][c] = "#"
            # 递归找寻
            for r_offset, c_offset in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                new_r, new_c = r + r_offset, c + c_offset
                if new_r < 0 or new_r >= m or new_c < 0 or new_c >= n:
                    continue
                # 判断是否有效
                if board[new_r][new_c] not in cur_node:
                    continue
                dfs(new_r, new_c, cur_node)
            # 还原当前位置
            board[r][c] = letter

        # 遍历矩阵找寻匹配的单词
        for i in range(m):
            for j in range(n):
                if board[i][j] in tree:
                    dfs(i, j, tree)
        return result
