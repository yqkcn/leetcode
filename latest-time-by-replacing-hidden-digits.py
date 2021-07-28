class Solution:
    def maximumTime(self, time: str) -> str:
        a, b, c, d = time[0], time[1], time[3], time[4]
        if a == "?":
            if b == "?":
                a = "2"
                b = "3"
            elif b in "0123":
                a = "2"
            else:
                a = "1"
        if b == "?":
            if a in "01":
                b = "9"
            else:
                b = "3"
        if c == "?":
            c = "5"
        if d == "?":
            d = "9"
        return f"{a}{b}:{c}{d}"
