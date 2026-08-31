/*
Find all numbers that appear at least three times consecutively.
Return the result table in any order.
The result format is in the following example.
*/
select distinct C.num as "ConsecutiveNums" from Logs as C
where exists
(select A.id from Logs as A
where exists (select B.id from Logs as B where B.id = A.id + 1 and B.num = A.num)
and A.id = C.id + 1 and A.num = C.num)
