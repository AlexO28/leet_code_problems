/* There is a queue of people waiting to board a bus. However, the bus has a weight limit of 1000 kilograms, so there may be some people who cannot board.

Write a solution to find the person_name of the last person that can fit on the bus without exceeding the weight limit. The test cases are generated such that the first person does not exceed the weight limit.*/

/* Write your T-SQL query statement below */

with temp as
(select A.turn, sum(B.weight) as cumsum from Queue as A
inner join
Queue as B
on B.turn <= A.turn
group by A.turn
having sum(B.weight) <= 1000)
select person_name from Queue
where turn in (select max(turn) as turn
from temp)
