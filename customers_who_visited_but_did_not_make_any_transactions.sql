/* Write your T-SQL query statement below */

select customer_id, count(visit_id) as count_no_trans
from
(select Visits.customer_id, Visits.visit_id from Visits 
left join Transactions
on Visits.visit_id = Transactions.visit_id
where Transactions.visit_id is null) as A
group by customer_id
