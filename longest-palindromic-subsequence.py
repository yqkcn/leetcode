class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dq = []
        for i in range(length):
            dq.append([0]*length)
        for i in range(length):
            # 起止坐标相等时，字符串长度为1
            dq[i][i] = 1
        for i in range(length - 1, -1, -1):
            for j in range(i+1, length):
                if s[i] == s[j]:
                    dq[i][j] = dq[i+1][j-1] + 2
                else:
                    dq[i][j] = max(dq[i+1][j], dq[i][j-1])
        return dq[0][length-1]
