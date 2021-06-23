from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # 按照 X 轴坐标排序
        rectangles = sorted(rectangles, key=lambda x: (x[0],x[2]))
        # 计算总面积
        area = 0
        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
        # 找到重叠面积并减去
        length = len(rectangles)
        for i in range(length - 1):
            x1, y1, x2, y2 = rectangles[i]
            for j in range(i + 1, length):
                x3, y3, x4, y4 = rectangles[j]
                # 已排序，x1 肯定小于等于 x3
                # 没有重叠
                if x2 <= x3 or y2 <= y3 or y1 >= y4:
                    break
                # 重叠面积计算
                # 重叠部分X轴起始坐标为 x1 和 x3 较大者，终止坐标为 x2 和 x4 较小者
                # 重叠部分y轴起始坐标为 y1 和 y3 较大者，终止坐标为 y2 和 y4 较小者
                area -= (min(x2, x4) - max(x1, x3)) * (min(y2, y4) - max(y1, y3))
                print(i, j , area)
        # 取模
        return area % (10 ** 9 + 7)


if __name__ == '__main__':
    Solution().rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]])
