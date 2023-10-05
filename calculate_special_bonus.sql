/*Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.*/

/* Write your T-SQL query statement below */

select employee_id,
case when (employee_id % 2 = 1) and (substring(Employees.name, 1, 1) != 'M')
then salary else 0 end as bonus
from Employees
order by employee_id
