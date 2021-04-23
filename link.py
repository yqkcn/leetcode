from typing import List


def link(grid: List[List[int]], x1: int, y1: int, x2: int, y2: int) -> bool:
    r1 = r2 = c1 = c2 = True
    step = 1 if x1 <= x2 else -1
    x = x1
    while x != x2:
        x += step
        if grid[x][y1] == 1:
            r1 = False
        if grid[x][y2] == 1:
            r2 = False

    step = 1 if y1 <= y2 else -1
    y = y1
    while y != y2:
        y += step
        if grid[x1][y] == 1:
            c1 = False
        if grid[x2][y] == 1:
            c2 = False

    return (r1 and c2) or (c1 and r2)
