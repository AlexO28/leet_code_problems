/* Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is 'N'.

Write a solution to report all the employees with their primary department. For employees who belong to one department, report their only department.*/

/* Write your T-SQL query statement below */

with A as
(select * from Employee as A where exists
(select employee_id, count(department_id) as cnt from Employee
where Employee.employee_id = A.employee_id
group by employee_id
having count(department_id) = 1))
(select employee_id, department_id from Employee where primary_flag = 'Y')
union 
(select employee_id, department_id from A)
