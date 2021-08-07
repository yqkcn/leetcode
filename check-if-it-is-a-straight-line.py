from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        y = coordinates[0][1] - coordinates[1][1]
        x = coordinates[0][0] - coordinates[1][0]
        for i in range(2, len(coordinates)):
            _y = coordinates[i - 1][1] - coordinates[i][1]
            _x = coordinates[i - 1][0] - coordinates[i][0]
            if y * _x != x * _y:
                return False
        return True
