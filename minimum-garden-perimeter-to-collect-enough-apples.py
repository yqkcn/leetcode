class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        total = 0
        num = 0
        while total < neededApples:
            num += 1
            total += 12 * num ** 2
        print(num)
        return num * 8


if __name__ == '__main__':
    Solution().minimumPerimeter(13)