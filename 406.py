from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        highs, highs_sort = set(), defaultdict(list)
        for human in people:
            highs.add(human[0])
            highs_sort[human[0]].append(human)
        res = []
        for high in reversed(sorted(highs)):
            for human in sorted(highs_sort[high], key=lambda x: x[1]):
                res.insert(human[1], human)
        return res


if __name__ == '__main__':
    s = Solution()
    s.reconstructQueue([[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]])
