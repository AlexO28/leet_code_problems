---Write a solution to find the employees who are high earners in each of the departments.

WITH UT AS
(SELECT departmentId, salary,
 ROW_NUMBER() OVER (PARTITION BY departmentId
ORDER BY salary DESC) AS rn
FROM (SELECT DISTINCT departmentId, salary from Employee) as E)
SELECT DISTINCT Department.name as [Department], Employee.name as [Employee], Employee.salary as [Salary]
FROM Employee
INNER JOIN UT
ON (Employee.salary = UT.salary) and (Employee.departmentId = UT.departmentId)
INNER JOIN Department
ON (Employee.departmentId = Department.id)
WHERE UT.RN <= 3
