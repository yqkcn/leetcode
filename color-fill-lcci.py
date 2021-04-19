from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image
        m, n = len(image), len(image[0])
        target = image[sr][sc]
        queue = {(sr, sc)}
        processed = set()
        while queue:
            r, c = queue.pop()
            if (r, c) in processed:
                continue
            processed.add((r, c))
            if image[r][c] == target:
                image[r][c] = newColor
                for i, j in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
                    if 0 <= i < m and 0 <= j < n and (i, j) not in processed:
                        queue.add((i, j))
        return image
