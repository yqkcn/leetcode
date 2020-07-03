from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        import collections
        path = collections.defaultdict(list)
        for m, n in prerequisites:
            if m == n:
                return False
            path[m].append(n)
        for i in range(numCourses):
            mark = {i}
            values = path[i]
            while values:
                cur = []
                for num in values:
                    if num in mark:
                        continue
                    if i in path[num]:
                        return False
                    mark.add(num)
                    cur.extend(path[num])
                values = list(set(cur))
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(2, [[1, 0]]))
    print(s.canFinish(5, [[1, 2], [2, 3], [3, 4], [1, 1]]))
