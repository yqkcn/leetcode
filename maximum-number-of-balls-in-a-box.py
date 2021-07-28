class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        import collections

        counter = collections.defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            num = sum(int(x) for x in str(i))
            counter[num] += 1
        return max(counter.values())
