from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        length = len(arr)
        up = [1] * length
        down = [1] * length
        for i in range(1, length):
            if arr[i] > arr[i-1]:
                up[i] = down[i-1] + 1
            elif arr[i] < arr[i-1]:
                down[i] = up[i-1] + 1
        return max(max(up), max(down))


if __name__ == '__main__':
    Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9])
