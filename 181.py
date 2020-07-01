# Write your MySQL query statement below
"SELECT Employee.Name as Employee FROM Employee LEFT JOIN Employee l ON Employee.ManagerId = l.Id WHERE Employee.ManagerId IS NOT NULL AND Employee.Salary > l.Salary"
