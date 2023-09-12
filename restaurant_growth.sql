/*You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). average_amount should be rounded to two decimal places.

Return the result table ordered by visited_on in ascending order.*/

/* Write your T-SQL query statement below */

with payments as
(select visited_on, sum(amount) as amount from Customer group by visited_on)
select * from
(
 select B.visited_on, sum(C.amount) as amount,
 round(cast (sum(C.amount) as float)/7, 2) as average_amount
  from payments as B inner join payments as C
 on B.visited_on <= dateadd(day, 6, C.visited_on) and B.visited_on >= C.visited_on 
 group by B.visited_on
) as A
where A.visited_on >= (select dateadd(day, 6, min(visited_on)) from Customer)
order by A.visited_on
