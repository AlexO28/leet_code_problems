/*Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).*/
select case when B.indicator = 0 then null else SecondHighestSalary end as SecondHighestSalary from 
(select min(salary) as SecondHighestSalary, max(salary)-min(salary) as indicator from
(select distinct salary from Employee order by salary desc limit 2) as A) as B
