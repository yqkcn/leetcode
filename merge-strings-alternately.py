class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1, word2 = list(word1), list(word2)
        word = []
        while word1 and word2:
            word.append(word1.pop(0))
            word.append(word2.pop(0))
        word.extend(word1)
        word.extend(word2)
        return "".join(word)
