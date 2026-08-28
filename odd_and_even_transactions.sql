/*
Write a solution to find the sum of amounts for odd and even transactions for each day. If there are no odd or even transactions for a specific date, display as 0.
Return the result table ordered by transaction_date in ascending order.
*/
select 
transaction_date,
sum(case when amount % 2 = 1 then amount else 0 end) as odd_sum,
sum(case when amount % 2 = 0 then amount else 0 end) as even_sum
from transactions
group by transaction_date
