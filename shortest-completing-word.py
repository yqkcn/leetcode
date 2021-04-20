from typing import List
import string


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        from collections import Counter

        counter = Counter([i.lower() for i in licensePlate if i in string.ascii_letters])
        res = ""
        for word in words:
            _counter = Counter([i.lower() for i in word if i in string.ascii_letters])
            match = True
            for k, v in counter.items():
                if _counter[k] < v:
                    match = False
                    break
            if not match:
                continue
            if not res or len(word) < len(res):
                res = word
        return res
