class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        if x >= y:
            return x - y
        # 偶数
        if not y % 2:
            return 1 + self.brokenCalc(x, y // 2)
        # 奇数
        return 1 + self.brokenCalc(x, y + 1)

if __name__ == '__main__':
    Solution().brokenCalc(2, 3)