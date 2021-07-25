import string


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        new_s = []
        for letter in s:
            new_s.append(string.ascii_letters.index(letter) + 1)
        new_s = "".join(str(x) for x in new_s)
        for i in range(k):
            num = sum([int(x) for x in new_s])
            new_s = str(num)
        return int(new_s)
