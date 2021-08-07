from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, e = 0, len(numbers) - 1
        while True:
            num = numbers[s] + numbers[e]
            if num == target:
                break
            elif num > target:
                e -= 1
            else:
                s += 1
        return [s, e]
