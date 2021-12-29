class BrowserHistory:

    def __init__(self, homepage: str):
        self.values = [homepage]
        self.idx = 0


    def visit(self, url: str) -> None:
        self.values = self.values[:self.idx + 1]
        self.values.append(url)
        self.idx += 1


    def back(self, steps: int) -> str:
        self.idx = max(0, self.idx - steps)
        return self.values[self.idx]


    def forward(self, steps: int) -> str:
        self.idx = min(len(self.values) - 1, self.idx + steps)
        return self.values[self.idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)