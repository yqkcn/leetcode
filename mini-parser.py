"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()
        stack = []
        for w in s:
            if w == "[":
                if stack and not stack[-1]:
                    stack[-1] = w
                else:
                    stack.append(w)
            elif w == ",":
                # 开始新的元素
                stack.append("")
            elif w.isdigit():
                if stack and stack[-1].isdigit():
                    stack[-1] += w
                else:
                    stack.append(w)
            elif w == "]":
                _cur = []
                while stack[-1] != "[":
                    cur = stack.pop()
                    if not cur:
                        continue
                    if isinstance(cur, NestedInteger):
                        _cur.append(cur)
                    elif isinstance(cur, list):
                        n = NestedInteger()
                        for x in cur[::-1]:
                            n.add(x)
                        _cur.append(n)
                    else:
                        _cur.append(NestedInteger(int(cur)))
                stack.pop()
                stack.append(_cur)
        stack = stack[0]
        if not isinstance(stack, list):
            return NestedInteger(int(stack))
        if len(stack) == 1:
            return stack[0]
        res = NestedInteger()
        for x in stack[::-1]:
            res.add(x)
        return res


if __name__ == '__main__':
    Solution().deserialize("324")
