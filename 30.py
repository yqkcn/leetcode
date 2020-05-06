from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words: return []
        one_word = len(words[0])
        all_len = len(words) * one_word
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, n - all_len + 1):
            tmp = s[i:i + all_len]
            c_tmp = []
            for j in range(0, all_len, one_word):
                c_tmp.append(tmp[j:j + one_word])
            if Counter(c_tmp) == words:
                res.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(s.findSubstring("aaa", ["a", "a"]))
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
