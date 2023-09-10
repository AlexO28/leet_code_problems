# Write your MySQL query statement below

select project_id, ifnull(round(avg(experience_years), 2), 0) as average_years
    from Project left join Employee
    on Project.employee_id = Employee.employee_id
    group by project_id
