class Solution:
    def countTriples(self, n: int) -> int:
        answer = 0
        max_num = n * n
        for i in range(1, n - 1):
            num1 = i * i
            for j in range(i + 1, n):
                num2 = j * j
                if num1 + num2 > max_num:
                    break
                for k in range(j + 1, n + 1):
                    num3 = k * k
                    if num1 + num2 == num3:
                        answer += 1
                        break
                    elif num1 + num2 < num3:
                        break
        return answer * 2


if __name__ == '__main__':
    Solution().countTriples(10)
