/*Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.*/
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
RETURN QUERY (
select case when (B.indicator < n) or (n <= 0) then null else SecondHighestSalary end from 
(select min(A.salary) as SecondHighestSalary, count(A.salary) as indicator from
(select distinct C.salary from Employee as C order by C.salary desc limit abs(n)) as A) as B
);
END;
$$ LANGUAGE plpgsql;
