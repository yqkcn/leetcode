from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        res = [1, 1]
        for i in range (2, rowIndex + 1):
            tmp = [0] + res + [0]
            cur = [0] * (i + 1)
            l, r = 0, i
            while l <= r:
                cur[l] = tmp[l] + tmp[l + 1]
                cur[r] = tmp[r] + tmp[r + 1]
                l += 1
                r -= 1
            res = cur
        return res


if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        print(s.getRow(i))