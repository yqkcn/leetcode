class Solution:
    # def countVowelPermutation(self, n: int) -> int:
    #     # dq[i][j] 表示长度为i+1以j结尾的字符串的个数，j为1~5对应 a e i o u
    #     dq = []
    #     for i in range(n):
    #         dq.append([0] * 5)
    #     # 初始化长度为1的情况
    #     dq[0] = [1] * 5
    #     for i in range(1, n):
    #         # a 前面可以是 e, i, u
    #         dq[i][0] += dq[i - 1][1] + dq[i - 1][2] + dq[i - 1][4]
    #         # e 前面可以是 a, i
    #         dq[i][1] += dq[i - 1][0] + dq[i - 1][2]
    #         # i 前面可以是 e, o
    #         dq[i][2] += dq[i - 1][1] + dq[i - 1][3]
    #         # o 前面可以是 i
    #         dq[i][3] += dq[i - 1][2]
    #         # u 前面可以是 i o
    #         dq[i][4] += dq[i - 1][2] + dq[i - 1][3]
    #     return sum(dq[-1]) % (10**9+7)
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        for j in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (10 ** 9 + 7)
