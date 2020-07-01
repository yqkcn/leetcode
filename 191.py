class Solution:
    def hammingWeight(self, n: int) -> int:
        return f"{n:b}".count("1")


if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(11111111111111111111111111111101))
