from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        if any(ranks.count(i) >= 3 for i in ranks):
            return "Three of a Kind"
        if any(ranks.count(i) == 2 for i in ranks):
            return "Pair"
        if len(set(ranks)) == 5:
            return "High Card"