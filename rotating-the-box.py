from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        if not box or not box[0]:
            return box
        m, n = len(box), len(box[0])
        new_box = []
        for i in range(n):
            new_box.append([x[i] for x in box][::-1])
        # 记录最小下标
        min_idx = [n - 1] * m
        for i in range(n - 1, -1, -1):
            for j in range(m):
                print(new_box)
                if new_box[i][j] == "#":
                    new_box[i][j] = "."
                    new_box[min_idx[j]][j] = "#"
                    min_idx[j] -= 1
                elif new_box[i][j] == "*":
                    min_idx[j] = i - 1
        return new_box

if __name__ == '__main__':
    Solution().rotateTheBox([["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]])