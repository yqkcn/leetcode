class CQueue:

    def __init__(self):
        self._list = []

    def appendTail(self, value: int) -> None:
        self._list.append(value)

    def deleteHead(self) -> int:
        if not self._list:
            return -1
        return self._list.pop(0)

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
