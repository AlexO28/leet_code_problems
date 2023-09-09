--Write a solution to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa)

/* Write your T-SQL query statement below */

update Salary
set sex = case when sex = 'm' then 'f' else 'm' end
