import bisect
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        answer = 0
        counter = {}
        counter_keys = []
        total = 0
        for num in nums:
            total += num
            if lower <= total <= upper:
                answer += 1
            # 上下限值
            _l, _u = total - upper, total - lower
            # 找到满足要求的区间
            left, right = bisect.bisect_left(counter_keys, _l), bisect.bisect_right(counter_keys, _u)
            answer += sum(counter[x] for x in counter_keys[left:right])
            if total not in counter:
                counter[total] = 1
                bisect.insort_left(counter_keys, total)
            else:
                counter[total] += 1
        return answer


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        res, pre, now = 0, [0], 0
        for n in nums:
            now += n
            res += bisect.bisect_right(pre, now - lower) - bisect.bisect_left(pre, now - upper)
            bisect.insort(pre, now)
        return res

if __name__ == '__main__':
    print(Solution().countRangeSum(nums=[-2, 5, -1], lower=-2, upper=2))
