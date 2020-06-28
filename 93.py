from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def _process(cur, _s):
            if not cur[-1] or int(cur[-1]) > 255:
                return
            if len(cur[-1]) > 1 and cur[-1].startswith("0"):
                return
            if len(cur) == 4:
                if not _s:
                    res.append(cur)
            for i in range(1, 4):
                _process(cur + [_s[:i]], _s[i:])

        if len(s) > 12:
            return []
        res = []
        for i in range(1, 4):
            _process([s[:i]], s[i:])
        return list(set(".".join(_) for _ in res))


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))
    print(s.restoreIpAddresses("010010"))
