from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range (2, numRows):
            tmp = [0] + res[i - 1] + [0]
            cur = [0] * (i + 1)
            l, r = 0, i
            while l <= r:
                cur[l] = tmp[l] + tmp[l + 1]
                cur[r] = tmp[r] + tmp[r + 1]
                l += 1
                r -= 1
            res.append(cur)
        return res


if __name__ == '__main__':
    s = Solution()
    for i in range(8):
        print(s.generate(i))
