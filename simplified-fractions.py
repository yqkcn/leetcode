from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        # 分母
        for i in range(2, n + 1):
            ans.append(f"1/{i}")
            # 分子
            for j in range(2, i):
                # 判断是否是最简分数
                if i % j == 0:
                    continue
                flag = True
                for k in range(2, j):
                    if i % k == 0 and j % k == 0:
                        flag = False
                        break
                if flag:
                    ans.append(f"{j}/{i}")
        return ans
