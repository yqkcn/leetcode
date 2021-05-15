class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join(x[:-1] for x in sorted(s.split(" "), key=lambda y: y[-1]))
