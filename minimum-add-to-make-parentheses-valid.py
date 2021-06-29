class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        left = 0
        for letter in s:
            if letter == "(":
                left += 1
            else:
                if left:
                    left -= 1
                else:
                    res += 1
        return res + left
