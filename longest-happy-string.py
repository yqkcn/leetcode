class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = []
        choices = [[a, "a"], [b, "b"], [c, "c"]]
        while True:
            choices.sort(key=lambda x: x[0], reverse=True)
            success = False
            for i, choice in enumerate(choices):
                num, char = choice
                if not num:
                    continue
                # 能否添加
                if len(chars) >= 2 and chars[-1] == char and chars[-2] == char:
                    continue
                chars.append(char)
                choices[i][0] -= 1
                success = True
                break
            if not success:
                return "".join(chars)


if __name__ == '__main__':
    Solution().longestDiverseString(2, 8, 10)
