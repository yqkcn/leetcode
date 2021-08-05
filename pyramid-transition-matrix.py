from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        import collections
        import functools

        _map = collections.defaultdict(list)
        for allow in allowed:
            _map[allow[:2]].append(allow[-1])

        @functools.lru_cache(None)
        def dfs(prefix, cur) -> bool:
            if len(cur) == 1:
                # 堆到塔尖
                if not prefix:
                    return True
                # 下一层
                return dfs("", prefix)
            # 无法进行下去
            if cur[:2] not in _map:
                return False
            # 下一个元素
            for a in _map[cur[:2]]:
                if dfs(prefix + a, cur[1:]):
                    return True
            return False

        return dfs("", bottom)


if __name__ == '__main__':
    print(Solution().pyramidTransition("BCD", ["BCG", "CDE", "GEA", "FFF"]))
