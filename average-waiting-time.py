class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        cur = 0
        for a, t in customers:
            if cur <= a:
                total += t
                cur = a + t
            else:
                cur += t
                total += cur - a
        return total / len(customers)