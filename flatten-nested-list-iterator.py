# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.values = nestedList
        self._iter = self._next()
        self._next_value = None

    def next(self) -> int:
        return self._next_value

    def _next(self) -> int:
        for value in self.values:
            if value.isInteger():
                yield value.getInteger()
            else:
                v = NestedIterator(value.getList())
                while v.hasNext():
                    yield v.next()

    def hasNext(self) -> bool:
        try:
            self._next_value = next(self._iter)
            return True
        except Exception:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())