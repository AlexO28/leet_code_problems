/*
Write a solution to find the employees who earn more than their managers.
Return the result table in any order.
The result format is in the following example.
*/
select A.name as "Employee" from Employee as A
where exists
(select B.id from Employee as B
where A.managerId = B.id and A.salary > B.salary)
