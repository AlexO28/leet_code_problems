/*
Write a solution to find employees who have the highest salary in each of the departments.
Return the result table in any order.
The result format is in the following example.
*/
select Department.name as "Department", A.name as "Employee", A.salary as "Salary"
from Employee as A inner join
(select max(salary) as salary, departmentId
from Employee
group by departmentId) as B
on A.departmentId = B.departmentId and A.salary = B.salary
inner join Department
on A.departmentId = Department.Id
