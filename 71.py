class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for char in path:
            if char != "/":
                cur += char
                continue
            if not cur:
                cur = char
                continue
            if cur == "/":
                continue
            if cur == "/.":
                cur = "/"
                continue
            if cur == "/..":
                if stack:
                    stack.pop()
                cur = "/"
                continue
            stack.append(cur)
            cur = "/"
        if cur:
            if cur not in ["/", "/."]:
                if cur == "/..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(cur)
        return "".join(stack) if stack else "/"


if __name__ == '__main__':
    test_case = [
        ["/home/", "/home"],
        ["/../", "/"],
        ["/home//foo/", "/home/foo"],
        ["/a/./b/../../c/", "/c"],
        ["/a/../../b/../c//.//", "/c"],
        ["/a//b////c/d//././/..", "/a/b/c"],
    ]
    s = Solution()
    for case, expected in test_case:
        print(case)
        print(expected)
        print(s.simplifyPath(case))
        assert s.simplifyPath(case) == expected
