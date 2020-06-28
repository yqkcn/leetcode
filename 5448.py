# 给你一个字符串 path，其中 path[i] 的值可以是 'N'、'S'、'E' 或者 'W'，分别表示向北、向南、向东、向西移动一个单位。
# 机器人从二维平面上的原点 (0, 0) 处开始出发，按 path 所指示的路径行走。
# 如果路径在任何位置上出现相交的情况，也就是走到之前已经走过的位置，请返回 True ；否则，返回 False 。

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        position = (0, 0)
        _set = {(0, 0)}
        for char in path:
            if char == "N":
                position = (position[0], position[1] + 1)
            elif char == "S":
                position = (position[0], position[1] - 1)
            elif char == "E":
                position = (position[0] + 1, position[1])
            elif char == "W":
                position = (position[0] - 1, position[1])
            if position in _set:
                return True
            _set.add(position)
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPathCrossing("NESWW"))
