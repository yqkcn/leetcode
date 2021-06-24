from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        if length == 1:
            return 1
        if length == 2:
            return 3
        nums = []
        idx = 0
        while idx < length:
            # 结尾
            if idx == length - 1:
                nums.append(1)
                break
            # 相等，开始新的趋势
            if ratings[idx] == ratings[idx + 1]:
                nums.append(1)
                idx += 1
                continue
            num = 1
            # 上升趋势
            if ratings[idx] < ratings[idx + 1]:
                while idx < length - 1 and ratings[idx] < ratings[idx + 1]:
                    num += 1
                    idx += 1
                nums.append(num)
                idx += 1
            # 下降趋势
            else:
                while idx < length - 1 and ratings[idx] > ratings[idx + 1]:
                    num += 1
                    idx += 1
                nums.append(num)
                idx += 1
        # 计算总数，全部添加 ，然后删除重复的乖点部分
        # 谷底都按照1来处理，谷顶保留较大者
        # 趋势个数，求每个趋势的和，然后删掉起点和上一个趋势的终点中较小者
        res = 0
        for i, num in enumerate(nums):
            # 添加趋势个数
            res += num * (num + 1) / 2
            if i > 0:
                # 和上一个趋势比较，减去较小者
                res -= min(num, nums[i - 1])
        return res
