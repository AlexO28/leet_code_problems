/* Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.*/

/* Write your T-SQL query statement below */

select A.month, A.country,
trans_count,
case when approved_count is null then 0 else approved_count end as approved_count, trans_total_amount,
case when approved_total_amount is null then 0 else approved_total_amount end as approved_total_amount
from
(select
country, substring(cast(trans_date as character), 0, 8) as "month",
count(id) as trans_count, sum(amount) as trans_total_amount
from Transactions 
group by country, substring(cast(trans_date as character), 0, 8)) as A
left join
(select
country, substring(cast(trans_date as character), 0, 8) as "month",
count(id) as approved_count, sum(amount) as approved_total_amount
from Transactions 
where Transactions.state = 'approved'
group by country, substring(cast(trans_date as character), 0, 8)) as B
on A.country = B.country and A.month = B.month
