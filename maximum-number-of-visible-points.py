from typing import List


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        from math import atan2, degrees

        # 都减去原始点 x, y
        x0, y0 = location
        angles = []
        zero = 0
        # 遍历所有的点计算和观察点的角度
        for x, y in ([x - x0, y - y0] for x, y in points):
            # 原点
            if x == 0 and y == 0:
                zero += 1
            # y 轴
            elif x == 0:
                angles.append(90 if y > 0 else 270)
            # x 轴
            elif y == 0:
                angles.append(0 if x > 0 else 180)
            # 第一象限
            elif x > 0 and y > 0:
                angles.append(degrees(atan2(y, x)))
            # 第二象限
            elif x < 0 and y > 0:
                angles.append(degrees(atan2(-x, y)) + 90)
            # 第三象限
            elif x < 0 and y < 0:
                angles.append(degrees(atan2(-y, -x)) + 180)
            # 第四象限
            elif x > 0 and y < 0:
                angles.append(degrees(atan2(x, -y)) + 270)
        # 排序
        angles.sort()
        length = len(angles)
        # double 接起来
        angles = angles + [x + 360 for x in angles]
        ans = right = 0
        # 滑动窗口
        for i in range(length):
            while right <= len(angles) and angles[right] <= angles[i] + angle:
                right += 1
            ans = max(ans, right - i)
        return ans + zero

