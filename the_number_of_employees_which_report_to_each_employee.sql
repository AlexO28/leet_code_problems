/* Write your T-SQL query statement below */

select B.employee_id, Employees.name, B.reports_count, B.average_age from
(select A.employee_id, count(Employees.name) as reports_count, round(avg(cast(age as float)), 0) as average_age from 
(select distinct reports_to as employee_id from Employees
where reports_to is not null
) as A
inner join Employees
on A.employee_id = Employees.reports_to
group by A.employee_id) as B
inner join Employees
on B.employee_id = Employees.employee_id
order by B.employee_id
