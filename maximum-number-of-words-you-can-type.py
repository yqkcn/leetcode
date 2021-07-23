class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        num = 0
        words = text.split(" ")
        for word in words:
            cur = 1
            for letter in brokenLetters:
                if letter in word:
                    cur = 0
                    break
            num += cur
        return num
