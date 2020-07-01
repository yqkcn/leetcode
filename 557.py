class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(_[::-1] for _ in s.split(" "))