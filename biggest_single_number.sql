--A single number is a number that appeared only once in the MyNumbers table.

/* Write your T-SQL query statement below */

select max(A.num) as num from (select num, count(num) as freq from MyNumbers group by num having count(num) = 1) as A
