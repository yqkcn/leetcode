from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if n == 0:
                break
            if flowerbed[i] == 1:
                continue
            left = i - 1 < 0 or flowerbed[i - 1] == 0
            right = i + 1 >= len(flowerbed) or flowerbed[i + 1] == 0
            if left and right:
                flowerbed[i] = 1
                n -= 1
        return n == 0
