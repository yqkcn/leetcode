from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        import string

        widths = {k: v for k, v in zip(list(string.ascii_lowercase), widths)}
        idx = 0
        cur = 0
        res = 1
        while idx < len(s):
            if cur + widths[s[idx]] > 100:
                res += 1
                cur = 0
                continue
            cur += widths[s[idx]]
            idx += 1
        return [res, cur]
