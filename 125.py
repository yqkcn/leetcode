class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        _set = set(string.ascii_lowercase + string.digits)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l].lower() not in _set:
                l += 1
                continue
            if s[r].lower() not in _set:
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))