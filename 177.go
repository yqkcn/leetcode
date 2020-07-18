package main

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N := N-1
RETURN (
// Write your MySQL query statement below.
select Salary as getNthHighestSalary from Employee group by Salary order by Salary DESC limit N, 1

)
END
