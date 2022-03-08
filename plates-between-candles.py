from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        next_candle, pre_candle = {}, {}  # 前后蜡烛索引
        idx = -1
        counter = {}  # 累计计数
        cur = 0
        for i, char in enumerate(s):
            if char == "|":
                for j in range(idx + 1, i):
                    next_candle[j] = i
                    pre_candle[j] = idx
                next_candle[i] = i
                pre_candle[i] = i
                idx = i
            else:
                cur += 1
            counter[i] = cur
        # 处理最后一段
        for i in range(idx + 1, len(s)):
            pre_candle[i] = idx
            next_candle[i] = -1
            counter[i] = cur

        ans = []
        for m, n in queries:
            m = next_candle[m]
            n = pre_candle[n]
            if m >= n or m == -1 or n == -1:
                ans.append(0)
                continue
            ans.append(counter[n] - counter[m])
        return ans

if __name__ == '__main__':
    print(Solution().platesBetweenCandles("**|**|***|", [[2,5],[5,9]]))