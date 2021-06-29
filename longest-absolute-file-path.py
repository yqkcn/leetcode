class Solution:
    def lengthLongestPath(self, input: str) -> int:
        def _level(n: str) -> (str, int):
            new_n = n.lstrip("\t")
            return new_n, len(n) - len(new_n)

        res = 0
        stack = []
        names = input.split("\n")
        for name in names:
            n, level = _level(name)
            # 弹出低于等于当前层级的目录
            while stack and stack[-1][1] >= level:
                stack.pop()
            stack.append((n, level))
            if "." not in n:
                continue
            # 和已有最大长度比较
            cur = "/".join(x for x, _ in stack)
            if len(cur) > res:
                res = len(cur)
        return res


if __name__ == '__main__':
    Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
