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
        if s[0] != "[":
            return NestedInteger(int(s))
        stack = []
        for w in s:
            if w == "[" or w == "-":
                stack.append(w)
            elif w == ",":
                if not isinstance(stack[-1], NestedInteger):
                    stack[-1] = NestedInteger(int(stack[-1]))
            elif w.isdigit():
                if isinstance(stack[-1], str) and stack[-1] != "[":
                    stack[-1] += w
                else:
                    stack.append(w)
            elif w == "]":
                cur = []
                while True:
                    value = stack.pop()
                    if value == "[":
                        break
                    cur.insert(0, value if isinstance(value, NestedInteger) else NestedInteger(int(value)))
                node = NestedInteger()
                for x in cur:
                    node.add(x)
                stack.append(node)
        return stack[0]


if __name__ == '__main__':
    Solution().deserialize("324")
