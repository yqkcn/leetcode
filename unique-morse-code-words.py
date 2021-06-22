import string
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mol = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--",
               "-..-", "-.--", "--.."]
        _map = {x: y for x, y in zip(string.ascii_lowercase, mol)}
        _set = set()
        for word in words:
            _set.add("".join(_map[x] for x in word))
        return len(_set)
