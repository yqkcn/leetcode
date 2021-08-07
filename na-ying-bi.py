from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        answer = 0
        for coin in coins:
            a, b = coin // 2, coin % 2
            answer += a
            if b:
                answer += 1
        return answer
