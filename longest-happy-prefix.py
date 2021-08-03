class Solution:
    def longestPrefix(self, s: str) -> str:
        length = len(s)
        if length <= 1:
            return ""
        answer = 0
        for i in range(length - 1):
            if s[i] == s[-1] and s[:i + 1] == s[-(i + 1):]:
                answer = i + 1
        return s[:answer]


if __name__ == '__main__':
    Solution().longestPrefix("ababab")
