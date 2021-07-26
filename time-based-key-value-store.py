import bisect


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = {"vs": [], "ts": []}
        self.values[key]["vs"].append(value)
        self.values[key]["ts"].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        values = self.values.get(key)
        if not values:
            return ""
        vs, ts = values["vs"], values["ts"]
        index = bisect.bisect_right(ts, timestamp)
        if index == 0:
            return ""
        return vs[index - 1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
