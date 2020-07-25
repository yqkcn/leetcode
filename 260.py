from collections import Counter
class Solution:
    def singleNumber(self, nums: int) -> List[int]:
        counter = Counter(nums)
        return [_ for _ in counter if counter[_] == 1]