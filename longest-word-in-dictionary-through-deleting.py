class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            idx = 0
            for letter in s:
                if letter == word[idx]:
                    idx += 1
                if idx == len(word):
                    break
            if idx == len(word):
                return word
        return ""