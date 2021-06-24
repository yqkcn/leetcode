class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        nums = []
        idx = 0
        # 统计连续相同的数字
        while idx < len(s):
            num = 1
            while idx < len(s) - 1 and s[idx] == s[idx + 1]:
                num += 1
                idx += 1
            nums.append(num)
            idx += 1
        res = 0
        # 计算结果
        for i in range(len(nums) - 1):
            res += min(nums[i], nums[i + 1])
        return res
