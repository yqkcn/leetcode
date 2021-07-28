import collections
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        _words = collections.defaultdict(list)
        for word in words:
            _words[len(word)].append(word)
        ws = []
        for k in sorted(_words.keys(), reverse=True):
            ws.extend(sorted(_words[k]))
        _set = set(words)
        for w in ws:
            idx = 0
            while idx < len(w):
                if w[:idx + 1] in _set:
                    idx += 1
                    continue
                break
            if idx == len(w):
                return w
        return ""
