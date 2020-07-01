from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        res = [triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]]
        for row in triangle[2:]:
            cur = []
            for i, num in enumerate(row):
                if i == 0:
                    cur.append(res[0] + num)
                elif i == len(row) - 1:
                    cur.append(res[-1] + num)
                else:
                    cur.append(num + min(res[i], res[i - 1]))
            res = cur
        return min(res)


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
