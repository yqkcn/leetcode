from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        num = 0
        for cost in costs:
            if coins < cost:
                break
            coins -= cost
            num += 1
        return num