/*
Find all numbers that appear at least three times consecutively.
Return the result table in any order.
The result format is in the following example.
*/
select distinct C.num as ConsecutiveNums from Logs as C
where exists
(select D.num, D.id from (select A.num, A.id from Logs as A inner join Logs as B
on A.num = B.num and A.id = B.id + 1) as D
where D.num = C.num and D.id = C.id + 2)
