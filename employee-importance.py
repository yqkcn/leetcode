# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


from typing import List


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees = {x.id: x for x in employees}
        res = 0
        queue = [employees.get(id)]
        cache = set()
        while queue:
            employee = queue.pop()
            if employee.id in cache:
                continue
            cache.add(employee.id)
            res += employee.importance
            queue.extend(employees.get(x) for x in employee.subordinates)
        return res
