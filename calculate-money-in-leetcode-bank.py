class Solution:
    def totalMoney(self, n: int) -> int:
        a, b = n // 7, n % 7
        answer = 0
        for i in range(a):
            answer += 28 + i * 7
        for i in range(b):
            answer += a + 1 + i
        return answer
