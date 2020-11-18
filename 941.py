from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        max_num = max(arr)
        idx = arr.index(max_num)
        if idx == 0 or idx == len(arr) - 1:
            return False
        for i in range(idx):
            if arr[i] >= arr[i + 1]:
                return False
        for j in range(idx + 1, len(arr)):
            if arr[j] >= arr[j - 1]:
                return False
        return True


if __name__ == '__main__':
    Solution().validMountainArray([0, 3, 2, 1])
