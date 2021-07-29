import string


class Solution:
    def replaceDigits(self, s: str) -> str:
        idxes = {k: i for i, k in enumerate(string.ascii_lowercase)}
        s = list(s)
        for i in range(1, len(s), 2):
            s[i] = string.ascii_lowercase[idxes[s[i - 1]] + int(s[i])]
        return "".join(s)
