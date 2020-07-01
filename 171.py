class Solution:
    def titleToNumber(self, s: str) -> int:
        import string
        b = {k: i for i, k in enumerate(string.ascii_uppercase, 1)}
        res = 0
        for i, char in enumerate(s[::-1]):
            res += b[char] * (26 ** i)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber("AA"))
    print(s.titleToNumber("AB"))
