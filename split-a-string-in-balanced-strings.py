class Solution:
    def balancedStringSplit(self, s: str) -> int:
        score = 0
        answer = 0
        for i in s:
            if i == "L":
                score += 1
            else:
                score -= 1
            if score == 0:
                answer += 1
        return answer
