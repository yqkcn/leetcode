from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            _map = {}
            _set = set()
            flag = True
            for i in range(len(pattern)):
                if word[i] not in _map:
                    if pattern[i] in _set:
                        flag = False
                        break
                    _set.add(pattern[i])
                    _map[word[i]] = pattern[i]
                else:
                    if _map[word[i]] != pattern[i]:
                        flag = False
                        break
            if flag:
                result.append(word)
        return result
