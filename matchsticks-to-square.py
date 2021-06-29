class Solution:
    def makesquare(self, nums):
        total = sum(nums)
        target = total // 4
        sides = [0] * 4
        if total % 4:
            return False
        nums.sort(reverse=True)
        def dfs(idx):
            if idx == len(nums):
                return sides[0] == sides[1] == sides[2] == sides[3]
            for i in range(4):
                if sides[i] + nums[idx] <= target:
                    sides[i] += nums[idx]
                    if dfs(idx + 1):
                        return True
                    sides[i] -= nums[idx]
            return False

        return dfs(0)
