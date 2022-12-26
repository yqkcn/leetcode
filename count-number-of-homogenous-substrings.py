class Solution:
    def countHomogenous(self, s: str) -> int:
        length = len(s)
        res, left, right = 0, 0, 0
        while right < length:
            if right == length - 1:
                n = right - left + 1
                res += n * (n + 1) // 2
                break
            if s[right] == s[right + 1]:
                right += 1
            else:
                n = right - left + 1
                res += n * (n + 1) // 2
                left, right = right + 1, right + 1
        return res % (10 ** 9 + 7)
