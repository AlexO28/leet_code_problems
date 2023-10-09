/*Write a solution to report the IDs of all the employees with missing information. The information of an employee is missing if:

The employee's name is missing, or
The employee's salary is missing.
Return the result table ordered by employee_id in ascending order.*/

/* Write your T-SQL query statement below */

with A as
(select employee_id from Employees where Employees.name is not null),
B as
(select employee_id from Salaries where Salaries.salary is not null)
(select employee_id from A
where not exists (select employee_id from B where B.employee_id = A.employee_id))
union
(select employee_id from B
where not exists (select employee_id from A where A.employee_id = B.employee_id))
