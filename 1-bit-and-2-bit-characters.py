from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits = bits[:-1]
        while bits:
            num1 = bits.pop(0)
            if num1 == 0:
                continue
            if not bits:
                return False
            bits.pop(0)
        return True
