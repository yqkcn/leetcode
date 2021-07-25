from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        cache = {i: c for i, c in enumerate(change)}
        flag = False
        num = [int(x) for x in num]
        for i, letter in enumerate(num):
            if letter < cache[letter]:
                if not flag:
                    flag = True
                num[i] = cache[letter]
            elif letter > cache[letter]:
                if not flag:
                    continue
                break

        return "".join(str(x) for x in num)
   