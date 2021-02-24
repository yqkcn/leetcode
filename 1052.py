from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if len(customers) <= X:
            return sum(customers)
        angry_customers = [x if grumpy[i] else 0 for i, x in enumerate(customers)]
        cur = max_angry = sum(angry_customers[:X])
        for i in range(X, len(angry_customers)):
            cur = cur - angry_customers[i - X] + angry_customers[i]
            max_angry = max(cur, max_angry)
        return sum(customers) - sum(angry_customers) + max_angry


if __name__ == '__main__':
    n = Solution().maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], X=3)
    print(n)
