from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        answer = [first]
        for num in encoded:
            answer.append(answer[-1] ^ num)
        return answer
