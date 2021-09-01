from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 前缀差
        deltas = [0] * (n + 1)
        for s, e, n in bookings:
            deltas[s] += n
            deltas[e + 1] -= n
        answer = [0]
        for delta in deltas:
            answer.append(answer[-1] + delta)
        return answer[1:]
