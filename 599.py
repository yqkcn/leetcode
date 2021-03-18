from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map1 = {k: v for v, k in enumerate(list1)}
        map2 = {k: v for v, k in enumerate(list2)}
        public = {k: v + map2[k] for k, v in map1.items() if k in map2}
        res = sorted([(k, v) for k, v in public.items()], key=lambda x: x[1])
        return [k for k, v in res if v == res[0][1]]
