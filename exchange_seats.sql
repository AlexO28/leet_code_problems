--Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

/* Write your T-SQL query statement below */

with ids as
(select
case when A.id % 2 = 0 then A.id - 1 else A.id + 1 end as id, A.student
from Seat as A)
(select * from ids where id in (select id from Seat))
union 
(select * from Seat where id not in (select id from ids))
