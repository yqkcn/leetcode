from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = [0]
        while queue:
            next_queue = set()
            for room in queue:
                if room in visited:
                    continue
                visited.add(room)
                next_queue.update(rooms[room])
            queue = next_queue
        return len(visited) == len(rooms)
