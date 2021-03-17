from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = sorted(dictionary, key=lambda x: len(x))
        words = sentence.split(" ")
        res = []
        for word in words:
            for root in dictionary:
                if word.startswith(root):
                    word = root
                    break
            res.append(word)
        return " ".join(res)
