/*
Find the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.

Return the result table ordered by employee_id.
*/

/* Write your T-SQL query statement below */

select Employees.employee_id from Employees
where 
Employees.salary < 30000 and
Employees.manager_id is not null and
not exists 
(select A.employee_id from Employees as A where A.employee_id = Employees.manager_id)
order by Employees.employee_id
