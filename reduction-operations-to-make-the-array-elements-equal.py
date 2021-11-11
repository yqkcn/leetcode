class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        import collections
        counter = collections.Counter(nums)
        keys = sorted(counter.keys())
        ans = 0
        for i, key in enumerate(keys[1:], 1):
            ans += i * (counter[key])
        return ans