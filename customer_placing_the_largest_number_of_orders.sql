--Write a solution to find the customer_number for the customer who has placed the largest number of orders.

/* Write your T-SQL query statement below */
with A as
(select customer_number, count(order_number) as cnt from Orders group by customer_number)
select B.customer_number from
(select A.customer_number, A.cnt, (select max(A.cnt) from A) as maxnum from A) as B
where B.cnt = B.maxnum
