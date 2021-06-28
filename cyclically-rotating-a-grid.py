from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # 一层一层处理
        for i in range(min(m//2, n//2)):
            # 四个点坐标分别为 (i, i), (i, n-i), (m-i, i), (m-i, n-i)
            # 将这一层元素放入一个列表
            print(i)
            nums = [grid[r][i] for r in range(i, m-i-1)] +\
                   [grid[m-i-1][c] for c in range(i, n-i-1)] +\
                   [grid[r][n-i-1] for r in range(m-i -1, i, -1)] +\
                   [grid[i][c] for c in range(n-i-1, i, -1)]
            length = len(nums)
            offset = k % length
            new_nums = [nums[i-offset] for i in range(length)]
            # 修改矩阵的值
            idx = 0
            for r in range(i, m-i-1):
                grid[r][i] = new_nums[idx]
                idx += 1
            for c in range(i, n-i-1):
                grid[m-i-1][c] = new_nums[idx]
                idx += 1
            for r in range(m-i-1, i, -1):
                grid[r][n-i-1] = new_nums[idx]
                idx +=1
            for c in range(n-i-1, i, -1):
                grid[i][c] = new_nums[idx]
                idx += 1
        return grid

if __name__ == '__main__':
    Solution().rotateGrid([[10,1,4,8],[6,6,3,10],[7,4,7,10],[1,10,6,1],[2,1,1,10],[3,8,9,2],[7,1,10,10],[7,1,4,9],[2,2,4,2],[10,7,5,10]],1)