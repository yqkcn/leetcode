from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        import collections
        counter = collections.Counter(strs)
        strs = sorted(set(strs), key=lambda x: len(x), reverse=True)
        for i, char in enumerate(strs):
            # 有重复不考虑
            if counter[char] > 1:
                continue
            # 遍历长度大于等于自己的
            if not any(self._is_sub(char, x) for x in strs[:i]):
                return len(char)
        return -1

    def _is_sub(self, s1: str, s2: str) -> bool:
        """ 判断 s1 是否是 s2 的子序列 """
        idx1 = idx2 = 0
        while idx1 < len(s1) and idx2 < len(s2):
            if s1[idx1] == s2[idx2]:
                idx1 += 1
                idx2 += 1
            else:
                idx2 += 1
        return idx1 == len(s1)
