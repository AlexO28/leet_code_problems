/*
Write a solution to find the employees who earn more than their managers.
Return the result table in any order.
*/
select A.name as "Employee" from Employee as A
where A.managerId is not null and
exists (select B.id from Employee as B
where B.id = A.managerId and B.salary < A.salary)
