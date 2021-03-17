class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if not m or not n:
            return 0
        # dp[i][j]表示 s[:i] 的子序列中 t[:j]出现的次数
        dp = []
        for i in range(m):
            dp.append([0] * n)
            dp[i][0] = s[:i + 1].count(t[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i < j:
                    continue
                if s[i] == t[j]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().numDistinct(s="rabbbit", t="rabbit"))
