class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        counter_a = Counter(s)
        counter_b = Counter(t)
        for k, v in counter_b.items():
            if counter_a.get(k) != v:
                return k


if __name__ == '__main__':
    s = Solution()
    print(s.findTheDifference("abcd", "abcde"))
