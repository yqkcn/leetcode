class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self._min_values = []

    def push(self, x: int) -> None:
        self.values.append(x)
        if not self._min_values or x < self._min_values[-1]:
            self._min_values.append(x)
        else:
            self._min_values.append(self._min_values[-1])

    def pop(self) -> None:
        self._min_values.pop()
        self.values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self._min_values[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
