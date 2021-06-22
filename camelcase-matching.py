import string
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        return [self._is_match(x, pattern) for x in queries]

    def _is_match(self, query: str, pattern: str) -> bool:
        length1, length2 = len(query), len(pattern)
        idx1 = idx2 = 0
        while idx1 < length1 and idx2 < length2:
            if pattern[idx2] in string.ascii_uppercase:
                while idx1 < length1:
                    if query[idx1] in string.ascii_lowercase:
                        idx1 += 1
                        continue
                    if query[idx1] != pattern[idx2]:
                        return False
                    idx1 += 1
                    idx2 += 1
                    break
            else:
                while idx1 < length1:
                    if query[idx1] in string.ascii_uppercase:
                        return False
                    if query[idx1] != pattern[idx2]:
                        idx1 += 1
                        continue
                    idx1 += 1
                    idx2 += 1
                    break
        # 未包含
        if idx2 != length2:
            return False
        # 判断 query 剩下的字符有没有大写字符
        for i in range(idx1, length1):
            if query[i] in string.ascii_uppercase:
                return False
        return True


if __name__ == '__main__':
    Solution().camelMatch(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FB")
