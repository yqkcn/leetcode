class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        import collections

        counter = {}
        length = len(word)
        for i in range(length+1):
            counter[i] = collections.Counter(word[:i])

        res = 0
        for i in range(length):
            for j in range(i + 1, length+1):
                counter1 = counter[i]
                counter2 = counter[j]
                nums = [counter2[k] - counter1.get(k, 0) for k in counter2]
                if len([num for num in nums if num % 2]) <= 1:
                    res += 1
        return res
