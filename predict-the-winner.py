from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # 偶数必赢
        if not n % 2:
            return True
        # 奇数分两种，先取第一个和先取最后一个
        # 先取第一个，剩下的偶数个2号选手肯定能取到较大的一组
        num1 = nums[0]
        sum1 = sum(nums[i] for i in range(1, n) if not i % 2)  # 奇数位
        sum2 = sum(nums[i] for i in range(1, n) if i % 2)  # 偶数位
        if num1 + min(sum1, sum2) >= max(sum1, sum2):
            return True
        # 取最后一个
        num1 = nums[-1]
        sum1 = sum(nums[i] for i in range(n - 1) if not i % 2)  # 奇数位
        sum2 = sum(nums[i] for i in range(n - 1) if i % 2)  # 偶数位
        if num1 + min(sum1, sum2) >= max(sum1, sum2):
            return True
        # 输
        return False


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def dfs(s, e, step):
            if s == e:
                return nums[s] * step
            num1 = nums[s] * step + dfs(s + 1, e, -step)
            num2 = nums[e] * step + dfs(s, e - 1, -step)
            return max(num1, num2) if step == 1 else min(num1, num2)

        return dfs(0, len(nums) - 1, 1) >= 0
