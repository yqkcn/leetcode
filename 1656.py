from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.values = [[] for i in range(n+1)]
        self.ptr = 1


    def insert(self, id: int, value: str) -> List[str]:
        self.values[id] = value
        if self.ptr > id:
            return []
        res = []
        for i in range(self.ptr, len(self.values)):
            if not self.values[i]:
                self.ptr = i
                return res
            res.append(self.values[i])
        self.ptr = id + 1
        return res
