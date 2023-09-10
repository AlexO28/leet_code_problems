--Write a solution to find for each user, the join date and the number of orders they made as a buyer in 2019.

/* Write your T-SQL query statement below */

with temp as
(select user_id as buyer_id, join_date, count(distinct order_id) as orders_in_2019 from Users
left join Orders
on Users.user_id = Orders.buyer_id
where Orders.order_date >= '2019-01-01' and Orders.order_date <= '2019-12-31'
group by user_id, join_date),
temp2 as
(select user_id as buyer_id, join_date, 0 as orders_in_2019 from Users
where not exists (select temp.buyer_id from temp where temp.buyer_id = Users.user_id))
(select * from temp) union (select * from temp2)
