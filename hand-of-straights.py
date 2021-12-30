from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        import collections
        if len(hand) != groupSize * groupSize:
            return False
        counter = collections.Counter(hand)
        while counter:
            n = min(counter.keys())
            for i in range(groupSize):
                c = n + i
                if c not in counter:
                    return False
                if counter[c] == 1:
                    counter.pop(c)
                else:
                    counter[c] -= 1
        return True
