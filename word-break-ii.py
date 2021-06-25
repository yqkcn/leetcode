from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        length = len(s)
        word_set = set(wordDict)

        @lru_cache(None)
        def bfs(idx: int):
            if idx == length:
                return [[]]
            res = []
            for i in range(idx + 1, length + 1):
                word = s[idx:i]
                if word in word_set:
                    next_ans = bfs(i)
                    if next_ans:
                        res.extend(x + [word] for x in next_ans)
            return res

        ans = bfs(0)
        return [" ".join(x[::-1]) for x in ans]
