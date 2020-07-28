from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        if len(stones) == 2:
            return True
        target = stones[-1]
        _set = set(stones)
        cache = {}
        queue = [(1, 1)]
        while queue:
            if cache.get(queue[0]):
                queue.pop(0)
                continue
            cache[queue[0]] = True
            cur, step = queue.pop(0)
            for _s in [step - 1, step, step + 1]:
                if _s == 0 or cur + _s > target or cur + _s not in _set:
                    continue
                if cur + _s == target:
                    return True
                queue.append((cur + _s, _s))
        return False
