class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        num = 0
        for c in s:
            if c not in "()":
                stack.append(c)
            elif c == "(":
                num += 1
                stack.append(c)
            elif c == ")":
                if num:
                    num -= 1
                    stack.append(c)
        s = "".join(stack)[::-1]

        stack = []
        num = 0
        for c in s:
            if c not in "()":
                stack.append(c)
            elif c == ")":
                num += 1
                stack.append(c)
            elif c == "(":
                if num:
                    num -= 1
                    stack.append(c)
        return "".join(stack)[::-1]
