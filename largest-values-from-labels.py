from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        import collections
        counter = collections.Counter()
        num = ans = 0
        # 优先取大的，取得过程中保存标签值，超过限制就跳过
        for value, lable in sorted(zip(values, labels), reverse=True):
            if num >= numWanted:
                break
            if counter[lable] < useLimit:
                num += 1
                ans += value
                counter[lable] += 1
        return ans
